from string import ascii_lowercase
from time import time


class Alpha:
    __slots__ = list(ascii_lowercase)

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        lst = []
        for letter in ascii_lowercase:
            try:
                g = getattr(self, letter)
                lst.append(f'{letter}: {g}')
            except AttributeError:
                pass
        return ', '.join(lst)


class AlphaQ:
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            if k not in ascii_lowercase or len(k) != 1:
                raise AttributeError
            else:
                self.__dict__[k] = v

    def __setattr__(self, field, val):
        if field not in ascii_lowercase or len(field) != 1:
            raise AttributeError
        else:
            super().__setattr__(field, val)

    def __str__(self):
        lst = []
        for k,v in sorted([(k,v) for k,v in self.__dict__.items() if k in ascii_lowercase]):
            lst.append(f'{k}: {v}')
        return ', '.join(lst)

import sys
exec(sys.stdin.read())
