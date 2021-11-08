from math import *

def Calc(s, t, u):
    def func(x):
        a = eval(s, globals(), {'x': x})
        b = eval(t, globals(), {'x': x})
        return eval(u, globals(), {'x': a, 'y': b})
    return func

import sys
exec(sys.stdin.read())
