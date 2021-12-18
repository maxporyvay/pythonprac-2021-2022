start, fin = eval(input())
print([i for i in range(start,fin) if [j for j in range(2,i) if i % j == 0] == [] and i > 1])
