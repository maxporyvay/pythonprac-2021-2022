class dump(type):
    def __init__(self, name, parents, ns):
        for func in ns:
            if callable(ns[func]):
                def f(self, *args, **kwargs):
                    print(ns[func].__name__, args, kwargs)
                    return ns[func](*args, **kwargs)
                ns[func] = f
        print(ns)
        return super().__init__(name, parents, ns)
