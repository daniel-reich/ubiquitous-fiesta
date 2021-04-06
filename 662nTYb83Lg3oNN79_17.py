
def is_parallelogram(l):
    l.sort()
    return l[0][0] + l[3][0] == l[1][0] + l[2][0] and  l[0][1] + l[3][1] == l[1][1] + l[2][1]

