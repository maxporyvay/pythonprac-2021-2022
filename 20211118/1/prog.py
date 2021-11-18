def decdec(typee):
    def decor(fn):
        def newf(*args):
            for arg in args:
                if type(arg) is not typee:
                    raise TypeError
            return fn(*args)
        return newf
    return decor

def dumpc(cls):
    class newcl(cls):
        def __str__(self):
            res = super().__str__()
            return f">>>{res}<<<"
    return newcl
