import random
l = []
for i in range(9):
    a = int(random.random()*100 + 1)
    l.append(a)
pos = int(random.random()*9)
s = eval(input())
l.insert(pos,s)
print(l)
