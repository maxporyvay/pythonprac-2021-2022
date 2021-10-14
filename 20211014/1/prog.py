def fun(s, w, na, a_coeffs, nb, b_coeffs):
    pass

    l = str(input())
    lst = l.split(', ')
    s, w, *other = lst
    na, other = other[0], other[1:]
    a_coeffs, other = other[:int(na)+1], other[int(na)+1:]
    nb, b_coeffs = other[0], other[1:]
    #print(s, w, na, a_coeffs, nb, b_coeffs)

