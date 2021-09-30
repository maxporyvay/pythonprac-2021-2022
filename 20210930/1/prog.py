lst = list(eval(input()))
n = len(lst)
for i in range(n - 1):
    for j in range (n - i - 1):
        if (lst[j] ** 2 ) % 100 > (lst[j + 1] ** 2 ) % 100:
            lst[j],lst[j + 1] = lst[j + 1],lst[j]
print(lst)
