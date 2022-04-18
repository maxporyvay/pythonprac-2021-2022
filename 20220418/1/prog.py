def solveSquare(a, b, c):
    assert a != 0
    d = b * b - 4 * a * c
    if d < 0:
        return None
    else:
        x1 = (-b + d**0.5) / 2 / a
        x2 = (-b - d**0.5) / 2 / a
        return (min(x1, x2), max(x1, x2))
