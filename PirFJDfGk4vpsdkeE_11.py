
def help_bobby(size):
    l = []
    l2 = []
    t = 1
    for i in range(size):
        for j in range(size):
           l.append(t)
           t += 1
        l2.append(l)
        l = []
    s = size
    for i in range(size):
        l2[i][i] = 1
        l2[i][s-1] = 1
        s-=1
        for j in range(len(l2[i])):
            if l2[i][j] !=1:
                l2[i][j] = 0
    return l2

