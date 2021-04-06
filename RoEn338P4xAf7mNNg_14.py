
def shortest_path(lst):
    pnts = []
    for y, row in enumerate(lst):
        for x, n in enumerate(row):
            if n != '0':
                pnts.append((int(n), x, y))
    pnts.sort()
    return sum(abs(x2-x1)+abs(y2-y1) for (n1,x1,y1), (n2,x2,y2) in
               zip(pnts, pnts[1:]))

