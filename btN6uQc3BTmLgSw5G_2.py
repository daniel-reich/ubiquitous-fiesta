
def spiral_matrix(size, string):
    st = list(string + '+' * size**2)[:size**2]
    res = [[None]*size for _ in range(size)]
    x = y = (size-1) // 2
    dx, dy = 1, 0
    for path in range(2, 3*size):
        for i in range(path // 2):
            if not st: return res
            res[y][x] = st.pop(0)
            x, y = x+dx, y+dy
        dx, dy = -dy, dx

