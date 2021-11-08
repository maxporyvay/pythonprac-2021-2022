print(', '.join(sorted(filter(lambda s: s.count('TOR') == 2, [''.join(t) for t in __import__('itertools').product('TOR', repeat=int(input()))]))))
