from generator import Line

SIZE_D = 8

def reserveMemory(spaces: list):
    lines = []
    lines.append("section   .data")
    for space in spaces:
        name, size = space
        line = "{} TIMES {} DB 0".format(name, int(size/SIZE_D))
        lines.append(line)
    return lines