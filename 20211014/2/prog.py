from math import *

def scale(A, B, a, b, x):
    return (x - A)/(B - A)*(b - a) + a

def transpose(m):
    n = []
    for i in range(len(m[0])):
        n.append("".join([m[j][i] for j in range(len(m))]))
    return n

H, W, A, B, *F = input().split(" ")
H = int(H)
W = int(W)
A = float(A)
B = float(B)
F = "".join(F)
F = eval("lambda x: " + F)
X = [scale(0, H, A, B, i) for i in range(H)]
Y = [F(x) for x in X]
my, My = min(Y), max(Y)
mat = []
for y in Y:
    string = (int(scale(my, My, 0, W, y)) - 1) * " " + "*"
    string += (W - len(string)) * " "
    mat.append(string)
mat = transpose(mat)
mat.reverse()
for line in mat:
    print(line)
