class dump(type):
    def __new__(cls, name, parents, ns):
        for func in ns:
            if callable(ns[func]):
                def f(self, *args, func=ns[func], funcname=func, **kwargs):
                    print(funcname + ': ' + str(args) + ', ' + str(kwargs))
                    return func(self, *args, **kwargs)
                ns[func] = f
                ns[func].__name__ = func
        return super().__new__(cls, name, parents, ns)

import sys
exec(sys.stdin.read())
