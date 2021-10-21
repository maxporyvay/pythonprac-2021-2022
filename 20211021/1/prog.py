string = input()
print(len(set([(x,y) for (x,y) in zip(string.lower()[1:],string.lower()[:-1]) if x.isalpha() and y.isalpha()])))
