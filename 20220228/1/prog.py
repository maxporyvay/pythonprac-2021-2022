import textdistance


def dist(s1, s2, typo):
    return textdistance.levenshtein(s1, s2)
    

str1 = input()
str2 = input()
str3 = input()
assert ' ' not in str1
assert ' ' not in str2

res = dist(str1, str2, str3)
