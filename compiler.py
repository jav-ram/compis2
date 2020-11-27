from generator import Line
import re

SIZE_D = 8
REGISTERS = ['r8d', 'r9d', 'r10d', 'r11d']

def translate(symTable, iCode:list):
    lines = []

    # variables
    scopesSizes = symTable.getScopeSizes()
    rMemory = reserveMemory(scopesSizes)
    lines.extend(rMemory)

    # headers
    lines.append("section .text")
    lines.append("\tglobal  _start")
    lines.append("_start:")

    # body
    for i in iCode:
        lines.extend(translate_line(i))

    # modules

    # finish program
    lines.append("_end:")
    lines.append("\tmov     ebx, 0")
    lines.append("\tmov     eax, 1")
    lines.append("\tint     80h")
    return lines

def translate_line(line:Line):
    code = []
    if line.op == "MOV":
        # load var
        code.extend(loadVar(line.arg1))
        # do
        if isVar(line.arg2):
            # load var
            code.extend(loadVar(line.arg2, "ebx"))
            # assign
            code.append("\tmov    [ecx], [ebx]")
        else:
            code.append("\tmov    [ecx], {}".format(line.arg2))
    elif line.op == "+":
        code.extend(destOp(line, "add"))
    elif line.op == "-":
        code.extend(destOp(line, "sub"))
    elif line.op == "*":
        code.extend(destOpFunc(line, "mul"))
    elif line.op == "/":
        code.extend(destOpFunc(line, "div"))
    elif line.op == "&&":
        code.extend(destOp(line, "and"))
    elif line.op == "||":
        code.extend(destOp(line, "or"))
    return code

def reserveMemory(spaces: list):
    lines = []
    lines.append("section   .data")
    for space in spaces:
        (name, size) = space
        if size > 0:
            line = "\t{} TIMES {} DB 0".format(name, int(size/SIZE_D))
            lines.append(line)
    return lines

def getVar(s: str):
    dest = s.split("[")[0]
    print(s)
    offset = int(re.search("\[([^)]+)\]" , s).group().replace("[", "").replace("]", ""))
    return dest, offset

def loadVar(var:str, register:str="ecx"):
    code = []
    (dest, offset) = getVar(var)
    # calculate offset
    code.append("\tmov    {}, {}".format(register, dest))
    code.append("\tadd    {}, {}".format(register, int(offset/SIZE_D)))
    return code

def isVar(var:str):
    return "[" in var

def destOp(line:Line, op:str):
    code = []
    dest = "[ecx]"
    if "_" in line.dest:
        id = int(re.search("[0-9]+" , line.dest).group().replace("[", "").replace("]", ""))
        dest = REGISTERS[id]
    else:
        code.extend(loadVar(line.dest))

    if isVar(line.arg1):
        code.extend(loadVar(line.arg1, "ebx"))
    if isVar(line.arg2):
        code.extend(loadVar(line.arg2, "edx"))

    if isVar(line.arg1) and isVar(line.arg2):
        code.append("\t" + op + "    [ebx], [edx]")
        code.append("\tmov    {}, [ebx]".format(dest))
    elif isVar(line.arg1) and not isVar(line.arg2):
        arg2 = line.arg2
        if "_" in line.arg2:
            id = int(re.search("[0-9]+" , line.arg2).group().replace("[", "").replace("]", ""))
            arg2 = REGISTERS[id]
        code.append("\t" + op + "    [ebx], {}".format(arg2))
        code.append("\tmov    {}, [ebx]".format(dest))
    elif not isVar(line.arg1) and isVar(line.arg2):
        arg1 = line.arg1
        if "_" in line.arg1:
            id = int(re.search("[0-9]+" , line.arg1).group().replace("[", "").replace("]", ""))
            arg1 = REGISTERS[id]
        code.append("\tmov    ebx, {}".format(arg1))
        code.append("\t" + op + "    ebx, [edx]")
        code.append("\tmov    {}, ebx".format(dest))
    elif not isVar(line.arg1) and not isVar(line.arg2):
        arg1 = line.arg1
        arg2 = line.arg2
        if "_" in line.arg1:
            id = int(re.search("[0-9]+" , line.arg1).group().replace("[", "").replace("]", ""))
            arg1 = REGISTERS[id]
        if "_" in line.arg2:
            id = int(re.search("[0-9]+" , line.arg2).group().replace("[", "").replace("]", ""))
            arg2 = REGISTERS[id]
        code.append("\tmov    ebx, {}".format(arg1))
        code.append("\t" + op + "    ebx, {}".format(arg2))
        code.append("\tmov    {}, ebx".format(dest))
    return code

def destOpFunc(line:Line, op:str):
    code = []
    dest = "[ecx]"
    if "_" in line.dest:
        id = int(re.search("[0-9]+" , line.dest).group().replace("[", "").replace("]", ""))
        dest = REGISTERS[id]
    else:
        code.extend(loadVar(line.dest))

    if isVar(line.arg1):
        code.extend(loadVar(line.arg1, "ebx"))
    if isVar(line.arg2):
        code.extend(loadVar(line.arg2, "edx"))

    if isVar(line.arg1) and isVar(line.arg2):
        code.append("\tmov    eax, [ebx]")
        code.append("\t" + op + "    [edx]")
        code.append("\tmov    {}, eax".format(dest))
    elif isVar(line.arg1) and not isVar(line.arg2):
        arg2 = line.arg2
        if "_" in line.arg2:
            id = int(re.search("[0-9]+" , line.arg2).group().replace("[", "").replace("]", ""))
            arg2 = REGISTERS[id]
        code.append("\tmov    eax, [ebx]")
        code.append("\t" + op + "    {}".format(arg2))
        code.append("\tmov    {}, eax".format(dest))
    elif not isVar(line.arg1) and isVar(line.arg2):
        arg1 = line.arg1
        if "_" in line.arg1:
            id = int(re.search("[0-9]+" , line.arg1).group().replace("[", "").replace("]", ""))
            arg1 = REGISTERS[id]
        code.append("\tmov    eax, {}".format(arg1))
        code.append("\tmov    ebx, [edx]")
        code.append("\t" + op + "    ebx")
        code.append("\tmov    {}, eax".format(dest))
    elif not isVar(line.arg1) and not isVar(line.arg2):
        arg1 = line.arg1
        arg2 = line.arg2
        if "_" in line.arg1:
            id = int(re.search("[0-9]+" , line.arg1).group().replace("[", "").replace("]", ""))
            arg1 = REGISTERS[id]
        if "_" in line.arg2:
            id = int(re.search("[0-9]+" , line.arg2).group().replace("[", "").replace("]", ""))
            arg2 = REGISTERS[id]

        code.append("\tmov    eax, {}".format(arg1))
        code.append("\tmov    ebx, {}".format(arg1))
        code.append("\t" + op + "    ebx")
        code.append("\tmov    {}, eax".format(dest))
    
    return code