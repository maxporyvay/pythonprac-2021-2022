from itertools import tee, islice
def slide(seq, n):
    seq = iter(seq)
    i = 0
    flag = True
    while True:
        seq, seq1 = tee(seq)
        s = islice(seq1, i, i + n)
        s1, s2 = tee(s)
        l = len(list(s2))
        if l == 1:
            flag = False
        yield from s1
        i += 1
        if not flag:
            break

import sys
exec(sys.stdin.read())
