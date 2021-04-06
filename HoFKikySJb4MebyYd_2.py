
def transform_matrix(lst):
    lst2 = list(map(list, zip(*lst)))
    m = []
    rs = []
    cs = []
    for i in range(len(lst)):
        t = []
        for j in range(len(lst[i])):
            t.append(0)
        m.append(t)
​
    for i in range(len(lst)):
        rs.append(sum(lst[i]))
    for i in range(len(lst2)):
        cs.append(sum(lst2[i]))
​
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            m[i][j] = rs[i]-lst[i][j]+cs[j]-lst[i][j]
​
    return m

