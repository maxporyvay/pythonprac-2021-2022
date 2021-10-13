def Bisect (elem, seq):
    left = 0
    right = len(seq) - 1
    def lbinsearch (l, r):
        if (l >= r):
            return seq[l]
        else:
            m = (l + r) // 2
            if seq[m] >= elem:
                return lbinsearch (l, m)
            else:
                return lbinsearch (m + 1, r)
    if elem == lbinsearch(left, right):
        return True
    else:
        return False
    
x, s = eval(input())
print(Bisect(x, s))
