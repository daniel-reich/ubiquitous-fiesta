
def move(mat):
    n, m = len(mat), len(mat[0])
    i = [sum(l) for l in mat].index(1)
    j = mat[i].index(1)
    print(n, m, i, j)
    return move_coor(n, m, i, j)
​
​
def move_coor(n, m, i, j):
    def meh(str):
        if str == 'stop':
            ans = [[0]*m for _ in range(n)]
            ans[i][j] = 1
            return ans
        if str == 'up':
            return move_coor(n, m, (i-1)%n, j)
        if str == 'down':
            return move_coor(n, m, (i+1)%n, j)
        if str == 'right':
            return move_coor(n, m, i, (j+1)%m)
        if str == 'left':
            return move_coor(n, m, i, (j-1)%m)
        return move_coor(n, m, i, j)
    return meh

