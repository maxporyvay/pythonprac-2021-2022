class InvalidInput(Exception):
    pass

class BadTriangle(Exception):
    pass

def triangleSquare(s):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(s)
    except Exception:
        raise InvalidInput
    try:
        a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        b = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
        c = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
        p = (a + b + c) / 2
        sq = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    except Exception:
        raise BadTriangle
    if sq:
        return sq
    else:
        raise BadTriangle
    
while True:
    string = input()
    try:
        square = triangleSquare(string)
    except InvalidInput:
        print('Invalid input')
    except BadTriangle:
        print('Not a triangle')
    else:
        print(f'{square:.2f}')
        break
