import sys

def assign(x,y):
    if y != "0" and y != "1":
        raise ValueError

    varDict[x] = int(y)

def op(gate,x=0,y=0):
    if x != 0 and x != 1:
        x = varDict[x]
    if y != 0 and y != 1:
        y = varDict[y]

    if gate == "and":
        if x == 1 and y == 1:
            return 1
        else:
            return 0
    elif gate == "or":
        if x == 1 or y == 1:
            return 1
        else:
            return 0

def notOp(x=0):
    if x != 0 and x != 1:
        x = varDict[x]

    if x == 1:
        return 0
    else:
        return 1

def out(x):
    if x != 0 and x != 1:
        x = varDict[x]

    print x

varDict = {}

args = sys.argv
code = args[1].split(";")
for line in code:
    line = line.replace("\n", " ")
    items = line.split(" ")

    opDict = {
        "var":assign(items[1],items[3]),
        "0":op(items[1],items[0],items[2]),
        "1":op(items[1],items[0],items[2]),
        "not":notOp(items[1]),
        "out":out(items[1])
        }

    opDict[items[0]]
