
def largest_island(lst):
    def ones_position(lst):
        positions = []
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                if lst[i][j] == 1:
                    positions.append((i,j))
        return positions
    def connected(p,q):
        d1 = abs(p[0]-q[0])
        d2 = abs(p[1]-q[1])
        return d1 <1.5 and d2<1.5
    def pairwise_connected(positions):
        connect_mat = []
        for i,p in enumerate(positions):
            l = []
            for j,q in enumerate(positions):
                l.append(connected(p,q))
            connect_mat.append(l)
        return connect_mat
    positions = ones_position(lst)
    conn_mat = pairwise_connected(positions)
    return max(list(map(sum,conn_mat)))

