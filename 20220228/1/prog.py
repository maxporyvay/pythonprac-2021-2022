import textdistance


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

res = dist(str1, str2, str3)
