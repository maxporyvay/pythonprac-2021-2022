mat1 = []
mat2 = []
line = list(eval(input()))
n = len(line)
mat1.append(line)
for i in range(n-1):
    mat1.append(list(eval(input())))
for i in range(n):
    mat2.append(list(eval(input())))
mat3 = []
for i in range(n):
    mat3.append([])
    for j in range(n):
        mat3[i].append(0)
for i in range(n):
    for j in range(n):
        l1 = mat1[i]
        l2 = [mat2[p][j] for p in range(n)]
        mat3[i][j] = sum(x*y for (x,y) in zip(l1,l2))
for line in mat3:
    print(line)
