import textdistance
import multiprocessing as mp


def dist(s1, s2, typo):
    if typo == 'L':
        return textdistance.levenshtein(s1, s2)
    elif typo == 'D':
        return textdistance.damerau_levenshtein(s1, s2)
    else:
        return -1
    

str1 = input()
str2 = input()
str3 = input()
assert ' ' not in str1
assert ' ' not in str2

pool = mp.Pool(1)
process = pool.apply_async(dist, (str1, str2, str3))
try:
    res = process.get(timeout=1)
except mp.context.TimeoutError:
    res = -1
print(res)
