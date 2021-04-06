
def shortest_path(lst):
    brd = [list(i) for i in lst]; row = len(brd); col = len(brd[0])
    num = sorted([j for i in brd for j in i if j != '0'])
​
    pos = {}
    for i in num:
        pos[i] = ()
​
    for i in range(row):
        for j in range(col):
            if brd[i][j] in pos:
                pos[brd[i][j]] = (i, j)
​
    dic = sorted(pos.items(), key = lambda x: x[0][0])
    fin = [dic[i][1] for i in range(len(dic))]
​
    dis = []
    for i in range(len(fin)-1):
        dis.append(abs(fin[i][0]-fin[i+1][0]))
        dis.append(abs(fin[i][1]-fin[i+1][1]))
​
    return sum(dis)

