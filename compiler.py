from generator import Line
import re

SIZE_D = 8
REGISTERS = ['[r8d]', '[r9d]', '[r10d]', '[r11d]']

def translate(symTable, iCode:list):
    lines = []

    # variables
    scopesSizes = symTable.getScopeSizes()
    rMemory = reserveMemory(scopesSizes)
    lines.extend(rMemory)

    # headers
    lines.append("SECTION .text")
    lines.append("global  _start")
    lines.append("_start:")

    # body
    for i in iCode:
        lines.extend(translate_line(i))

    # modules
    # mul
    lines.append("mul:")
    lines.append("    mul     edx                     ;multiply eax*edx, result in edx:eax")
    lines.append("    ret")


    # finish program
    lines.append("_end:")
    lines.append("mov     ebx, 0")
    lines.append("mov     eax, 1")
    lines.append("int     80h")
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
            code.append("mov    [ecx], [ebx]")
        else:
            code.append("mov    [ecx], {}".format(line.arg2))
    elif line.op == "+":
        code.extend(destOp(line, "add"))
    elif line.op == "-":
        code.extend(destOp(line, "sub"))
    elif line.op == "*":
        code.extend(destOp(line, "mul"))
    return code

def reserveMemory(spaces: list):
    lines = []
    lines.append("section   .data")
    for space in spaces:
        (name, size) = space
        if size > 0:
            line = "{} TIMES {} DB 0".format(name, int(size/SIZE_D))
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
    code.append("mov    {}, {}".format(register, dest))
    code.append("add    {}, {}".format(register, int(offset/SIZE_D)))
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
        code.append(op + "    [ebx], [edx]")
        code.append(op + "    {}, [ebx]".format(dest))
    elif isVar(line.arg1) and not isVar(line.arg2):
        arg2 = line.arg2
        if "_" in line.arg2:
            id = int(re.search("[0-9]+" , line.arg2).group().replace("[", "").replace("]", ""))
            arg2 = REGISTERS[id]
        code.append(op + "    [ebx], {}".format(arg2))
        code.append(op + "    {}, [ebx]".format(dest))
    elif not isVar(line.arg1) and isVar(line.arg2):
        arg1 = line.arg1
        if "_" in line.arg1:
            id = int(re.search("[0-9]+" , line.arg1).group().replace("[", "").replace("]", ""))
            arg1 = REGISTERS[id]
        code.append("mov    ebx, 0")
        code.append(op + "    ebx, {}".format(arg1))
        code.append(op + "    ebx, [edx]")
        code.append(op + "    {}, ebx".format(dest))
    elif not isVar(line.arg1) and not isVar(line.arg2):
        arg1 = line.arg1
        arg2 = line.arg2
        if "_" in line.arg1:
            id = int(re.search("[0-9]+" , line.arg1).group().replace("[", "").replace("]", ""))
            arg1 = REGISTERS[id]
        if "_" in line.arg2:
            id = int(re.search("[0-9]+" , line.arg2).group().replace("[", "").replace("]", ""))
            arg2 = REGISTERS[id]
        code.append("mov    ebx, 0")
        code.append(op + "    ebx, {}".format(arg1))
        code.append(op + "    ebx, {}".format(arg2))
        code.append(op + "    {}, ebx".format(dest))
    return code