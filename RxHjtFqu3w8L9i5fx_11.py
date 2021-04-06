
def bell(n):
    if n == 1:
        return 1
    t = [[1]]
    for i in range(1,n):
        t.append([t[-1][-1]])
        for j in range(len(t[-2])):
            t[-1].append(t[-2][j]+t[-1][j])
    return t[-1][-1]

