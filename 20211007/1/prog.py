def Pareto(*lst):
    l = []
    for i in lst:
        flag = False
        for j in lst:
            if i[0] <= j[0] and i[1] <= j[1] and (i[0] < j[0] or i[1] < j[1]):
                flag = True
        if not flag:
            l.append(i)
    return tuple(l)
list_ = eval(input())
print(Pareto(*list_))
