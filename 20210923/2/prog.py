num = int(input())
n = 0
while num > 0:
    n += num
    if n > 21:
        break
    num = int(input())
else:
    n = num
print(n)
