import sys
seq = sys.stdin.buffer.read()
N = seq[0]
remains = seq[1:]
L = len(remains)
lst = []
for i in range(N):
    #lst.append(remains[round(i*L/N):round((i+1)*L/N)])
    lst.append(remains[i*L//N:(i+1)*L//N])
lst.sort()
st = seq[0:1] + b''.join(lst)
sys.stdout.buffer.write(st)
