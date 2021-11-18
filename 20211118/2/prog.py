class Num:
    def __get__(self, obj, cls):
        try:
            return obj._val
        except AttributeError:
            return 0
    def __set__(self, obj, val):
        if type(val) == int:
            obj._val = val
        else:
            obj._val = len(val)
    def __delete__(self, obj):
        obj._val = None
