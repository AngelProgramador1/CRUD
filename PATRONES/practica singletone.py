class Singletone(type):

    _intances = {}

    def __call__(cls, *args, **kwds):
        instancia= super().__call__(*args, **kwds)

        if cls not in cls._intances:

            cls._intances[cls] = instancia

            return cls._intances[cls]

class Human(metaclass=Singletone):
    def __init__(self, poder):
        self.poder = poder

p = Human(200)
print(p.poder)