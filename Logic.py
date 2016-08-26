import sys

opDict = {
    "var":assign(items[1],items[3]),
    "0":op(items[1],items[0],items[2]),
    "1":op(items[1],items[0],items[2]),
    "def":define(items[1],items[2])
    }
varDict = {}

def assign(x,y):
    if y != 0 and y != 1:
        raise ValueError

    varDict[x] = y

def op(gate,x,y):
    return logOpDict[gate]

args = sys.argv
if args[0][0] == '"' or args[0][0] == "'":
    code = args[0].split(";")
    for line in code:
        line = line.replace("\n", " ")
        items = line.split(" ")
        
