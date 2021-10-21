from collections import Counter

w = int(input())
text = input()
lst = text.strip().split()
for i in lst:
    dct.setdefault(i,0)
    dct[i] += 1
lst1 = Counter(lst)
print(dct)
print(dict(lst1))
