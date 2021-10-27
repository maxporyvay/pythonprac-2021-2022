from math import *

funcount = 0
linecount = 0
dctfun = {}

while (line := input())[0:4] != 'quit':
    linecount += 1
    if line[0] == ':':
        funcount += 1
        line = line[1:]
        fun, *params, expr = line.split()
        dctfun[fun] = (params, expr)
    else:
        f, *pars = line.split()
        dctlocals = {k: eval(v) for k,v in zip(dctfun[f][0], pars)}
        print(eval(dctfun[f][1], globals(), dctlocals))
else:
    linecount += 1
    funcount += 1
    line = line[6:-1]
    print(line.format(funcount, linecount))
