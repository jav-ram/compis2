from flask import Flask, render_template, request, session
from collections import OrderedDict
from main import compile

app = Flask(__name__, template_folder='./web', static_folder="./web/static")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = ".."

@app.route('/')
def inputView():
    source = ""
    if session.get('source'):
        source = session['source']
    return render_template('input.html', source=source)

@app.route('/', methods=['POST'])
def build():
    text = request.form['source-code']
    session['source'] = text
    # compile the text
    symTable, errors = compile(text)
    session['sym'] = symTable[0]
    session['typ'] = symTable[1]
    session['errors'] = errors
    print(errors)
    return render_template('input.html', source=text)

@app.route('/tree')
def treeView():
    return render_template('tree.html')

@app.route('/table')
def tableView():
    sym = {}
    typ = {}

    if session.get('sym'):
        sym = session['sym']
    if session.get('typ'):
        typ = session['typ']

    return render_template('table.html', sym=sym, typ=typ)

@app.route('/errors')
def errorView():
    errors = []
    prettyErr = {}

    if session.get('errors'):
        errors = session['errors']

    for error in errors:
        msg = error[0]
        line = int(error[1])


        if not line in prettyErr:
            prettyErr[line] = []

        prettyErr[line].append(msg)

    prettyErr = dict(sorted(prettyErr.items()))

    return render_template('errors.html', errors=prettyErr)