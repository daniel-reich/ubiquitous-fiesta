
def spiral_order(matrix):
    is_valid = lambda r, c: 0<=r<len(matrix) and 0<=c<len(matrix[0]) and matrix[r][c]!=-1
    order, dirns = [], [(0,1), (1,0), (0,-1), (-1,0)]
    r,c,d = 0,0,0
    while matrix[r][c] != -1:
        order.append(matrix[r][c])
        matrix[r][c] = -1
        nr, nc = r+dirns[d][0], c+dirns[d][1]
        if not is_valid(nr, nc):
            d = (d+1)%4
            nr, nc = r+dirns[d][0], c+dirns[d][1]
        r,c = nr,nc
    return order

