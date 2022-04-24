def solveSquare(a, b, c):
    if a != 0:
        d = b * b - 4 * a * c
        if d < 0:
            return None
        else:
            x1 = (-b + d**0.5) / 2 / a
            x2 = (-b - d**0.5) / 2 / a
            return (min(x1, x2), max(x1, x2))
    else:
        if b != 0:
            return (-c / b, -c / b)
        else:
            return None if c != 0 else '(-inf, +inf)'
        

class SquareIO():
    
    def inputCoeff(self, name):
        return input(f"Input {name}: ")
        
    def printResult(self, result):
        print(f"Solution: {result}")
        
        
def solve():
    io = SquareIO()
    a = io.inputCoeff('a')
    b = io.inputCoeff('b')
    c = io.inputCoeff('c')
    res = solveSquare(float(a), float(b), float(c))
    io.printResult(res)
