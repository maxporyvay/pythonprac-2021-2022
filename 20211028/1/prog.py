def fib(m, n):
    f0 = 1
    f1 = 1
    f2 = 2
    i = 0
    while True:
        if i >= m:
            yield f0
        if i == n:
            return f0
        f0, f1, f2 = f1, f2, f1 + f2
        i += 1

import sys
exec(sys.stdin.read())
