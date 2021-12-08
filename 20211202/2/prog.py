# version 3.9
import sys

class check(type):
    def __new__(cls, name, parents, ns):
        def check_annotations(self):
            for par, ann in self.__annotations__.items():
                if par not in self.__dict__ and par not in ns:
                    return False
                else:
                    try:
                        if par in self.__dict__:
                            if not isinstance(self.__dict__[par], ann):
                                return False
                        else:
                            if not isinstance(ns[par], ann):
                                return False
                    except TypeError:
                        return False
            return True
        ns['check_annotations'] = check_annotations
        return super().__new__(cls, name, parents, ns)

exec(sys.stdin.read())
