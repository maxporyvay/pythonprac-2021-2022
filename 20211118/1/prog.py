def objcount(cls):
    cls.counter = 0
    if '__init__' in cls.__dict__:
        old_init = cls.__init__
    else:
        old_init = None
    if '__del__' in cls.__dict__:
        old_del = cls.__del__
    else:
        old_del = None
    def __init__(self, *args, **kwargs):
        if old_init:
            old_init(self, *args, **kwargs)
        cls.counter += 1
    def __del__(self):
        cls.counter -= 1
        if old_del:
            old_del(self)
    cls.__init__ = __init__
    cls.__del__ = __del__
    return cls

import sys
exec(sys.stdin.read())
