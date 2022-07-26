from collections import Counter

w = int(input())
text = ''
while (line := input().strip()) != '':
    for char in line:
        if not (char.isalpha() or char in (' ','\n','\t')):
            line = line.replace(char, ' ')
    text += line
    text += ' '
lst = text.lower().split()
cntr = dict(Counter(lst))
dct = {k: v for k,v in cntr.items() if len(k) == w}
if dct != {}:
    m = dct[max(dct, key=dct.get)]
    print(*sorted([k for k,v in dct.items() if v == m]))
