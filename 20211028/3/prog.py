from itertools import product
print(', '.join(sorted(filter(lambda s: s.count('TOR') == 2, [''.join(t) for t in product('TOR', repeat=int(input()))]))))
