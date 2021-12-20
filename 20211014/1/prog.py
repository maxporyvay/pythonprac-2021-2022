from fractions import Fraction

def fun(s, w, na, a_coeffs, nb, b_coeffs):
    A = sum([Fraction(c) * Fraction(s) ** x for (c,x) in zip(reversed(a_coeffs), list(range(int(na) + 1)))])
    B = sum([Fraction(c) * Fraction(s) ** x for (c,x) in zip(reversed(b_coeffs), list(range(int(nb) + 1)))])
    return Fraction(A) / Fraction(B) == Fraction(w) if B != 0 else False

l = str(input())
lst = list(map(lambda s: s.strip(), l.split(',')))
s, w, *other = lst
na, other = other[0], other[1:]
a_coeffs, other = other[:int(na)+1], other[int(na)+1:]
nb, b_coeffs = other[0], other[1:]
print(fun(s, w, na, a_coeffs, nb, b_coeffs))

