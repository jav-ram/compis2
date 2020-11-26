import sys
import argparse
from antlr4 import *
from antlr4.tree.Trees import Trees

from decafeGenerated.grammars.DecafeLexer import DecafeLexer
from decafeGenerated.grammars.DecafeListener import DecafeListener

from visitor import MyVistor
from generator import IntermediateCodeGenerator
from compiler import reserveMemory, translate
from myparser import MyParser

from Tree import convertor

def setUpArgParser():
    argparser = argparse.ArgumentParser(description="Proyecto # 0")
    argparser.add_argument("-i", dest="input", help="input file", type=str)
    argparser.add_argument("-t", dest="showTree", help="If tag is on the tree will show", action='store_true')
    argparser.add_argument("-ns", dest="NoSymbolTable", help="If tag is present will not print symbol table", action="store_true" )

    return argparser.parse_args()

def compile(source, isFile=False):
    
    text = InputStream(source)
    if isFile:
        text = FileStream(source)
    lexer = DecafeLexer(text)
    stream = CommonTokenStream(lexer)
    parser = MyParser(stream)
    tree = parser.program()

    errors = parser.errMsg
    # print(Trees.toStringTree(tree, None, parser))
    tsymbol = MyVistor()
    # make symbol table
    tsymbol.visit(tree)
    # tsymbol.symTable.Print() # print table
    symTable = tsymbol.symTable.ToString() # get json of tables
    # make tree
    treeView, _ = convertor.convertInit(tree)(tree, 0)
    treeView.render('tree.gv', "./web/static/img")

    # intermediate code
    inCode = IntermediateCodeGenerator(tsymbol.symTable)
    inCode.visit(tree)

    iCode = []

    for l in inCode.lines:
        if l.type != "label":
            iCode.append("\t" + str(l))
        else:
            iCode.append(str(l))
    
    iCode = "\n".join(iCode)

    # compile to NASM
    symT = tsymbol.symTable
    for line in translate(symT, inCode.lines):
        print(line)

    print(iCode)

    errors.extend(tsymbol.errorMsg)

    errors = list(set(errors))

    return symTable, errors, iCode

def main(argv):
    args = setUpArgParser()

    symTable, errors, inCode = compile(args.input, isFile=True)
        

if __name__ == '__main__':
    main(sys.argv)