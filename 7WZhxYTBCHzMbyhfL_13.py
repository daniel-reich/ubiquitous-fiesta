
def next_move(x,y):
    for a,b in ((1,2),(2,1)):
        for sx in (1,-1):
            for sy in (1,-1):
                x1, y1 = x + sx*a, y + sy*b
                if all(1 <= z <= 8 for z in (x1,y1)):
                    yield x1, y1
​
def knight_bfs(a,b,c,d):
    start = (a,b)
    end = (c,d)
    if start == end:
        return 0
    st = [start]
    dist_to = {start:0}
    edge_to = {}
    while st:
        pos = st.pop(0)
        for m in next_move(*pos):
            if m == end:
                #path
                # path = [end]
                # edge_to[m] = pos
                # while edge_to[m] != start:
                #     path.append(edge_to[m])
                #     m = edge_to[m]
                # path.append(start)
​
                return dist_to[pos] + 1
            elif m not in dist_to:
                st.append(m)
                dist_to[m] = dist_to[pos] + 1
                edge_to[m] = pos
​
    return -1

