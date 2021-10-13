from math import *

def Calc(s, t, u):
    def func(x):
        a = eval(s, globals(), {'x': x})
        b = eval(t, globals(), {'x': x})
        return eval(u, globals(), {'x': a, 'y': b})
    return func

f1, f2, f = eval(input())
z = eval(input())
print((Calc(f1,f2,f))(z))
