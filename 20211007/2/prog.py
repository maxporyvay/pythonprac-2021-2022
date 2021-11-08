def SUB(a, b):
    if type(a) == type((1,2)) and type(b) == type((1,2)):
        return(tuple([x for x in a if x not in b]))
    elif type(a) == type([1,2]) and type(b) == type([1,2]):
        return([x for x in a if x not in b])
    else:
        return a - b

import sys
exec(sys.stdin.read())
