
def PrintError(errors, ctx):
    line = str(ctx.start.line)
    if isinstance(errors, str):
        if errors != "":
            print("Error in line " + line + ":")
            print("\t" + errors)
    if isinstance(errors, list):
        errors = flatten(errors)
        if len(errors) > 0:
            print("Errors in line " + line + ":")
            for error in errors:
                print("\t" + error)

def RecordError(errors, ctx):
    errs = []
    line = str(ctx.start.line)
    if isinstance(errors, str):
        if errors != "":
            errs.append((errors, line))
    if isinstance(errors, list):
        errors = flatten(errors)
        if len(errors) > 0:
            for error in errors:
                errs.append((error, line))
    return errs

def flatten(itr):
    if isinstance(itr, str):
        return
    t = tuple()
    for e in itr:
        try:
            t += flatten(e)
        except:
            t += (e,)
    return t