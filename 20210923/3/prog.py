n = int(input())
i = n
while i < n+3:
    j = n
    while j < n+3:
        sym = ' '
        if j == n+2:
            sym = '\n'
        res = i*j
        num = res
        rsum = 0
        while num > 0:
            rsum += (num % 10)
            num = num // 10
        if rsum == 6:
            res = ':=)'
        print(i, '*', j, '=', res, sep='', end=sym)
        j += 1
    i += 1
