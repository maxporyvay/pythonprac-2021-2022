from itertools import tee, islice
def slide(seq, n):
    if n <= 0:
        return ''
    seq = iter(seq)
    i = 0
    flag = True
    while True:
        seq, seq1, seqq, seqqq = tee(seq, 4)
        s = islice(seq1, i, i + n)
        s1, s2 = tee(s)
        l = len(list(s2))
        if l == 1 and n != 1:
            flag = False
        elif l == 1 and n == 1 and list(islice(seqq, i, i + 1)) == list(islice(seqqq, i, i + 2)):
            flag = False
        yield from s1
        i += 1
        if not flag:
            break

import sys
exec(sys.stdin.read())
