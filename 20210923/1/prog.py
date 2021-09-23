num = int(input())
a = b = c = '-'
if num % 25 == 0 and num % 2 == 0:
    a = '+'
if num % 25 == 0 and num % 2 == 1:
    b = '+'
if num % 8 == 0:
    c = '+'
print('A', a, 'B', b, 'C', c)
