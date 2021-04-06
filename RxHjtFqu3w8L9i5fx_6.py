
def bell(n):
    b = [[1]]
    for i in range(1,n):
        level = [b[-1][-1]]
        for j in range(i):
            level.append(level[-1]+b[-1][j])
        b.append(level)
    return b[-1][-1]

