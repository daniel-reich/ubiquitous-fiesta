
def hot_brick(t):
    st = [[25]*12]*10 + [[25]+[90]*10+[25]]
    dirs = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]
    for k in range(t):
        new = [[st[i][j] for j in range(12)] for i in range(11)]
        for i in range(1, 10):
            for j in range(1, 11):
                new[i][j] = round(sum(st[i+a][j+b] for (a, b) in dirs)/9,0)
        st = new
    return [[st[i][j] for j in range(1, 11)] for i in range(1, 11)]

