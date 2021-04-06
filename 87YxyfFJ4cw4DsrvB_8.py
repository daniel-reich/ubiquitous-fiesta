
def generate_rug(n):
    if n == 1:
        return [[0]]
    outer = (n - 1) // 2
    rug = []
    for _ in range(n):
        rug.append([outer] * n)
    rug[(n - 1) // 2][(n - 1) // 2] = 0
    for k in range(outer - 1, 0, -1):
        row1, row2 = outer - k, -(outer - k + 1)
        for col in range(row1, row1 + 2 * k + 1):
            rug[row1][col] = k
            rug[row2][col] = k
        col1, col2 = outer - k, -(outer - k + 1)
        for row in range(col1, col1 + 2 * k + 1):
            rug[row][col1] = k
            rug[row][col2] = k
    return rug

