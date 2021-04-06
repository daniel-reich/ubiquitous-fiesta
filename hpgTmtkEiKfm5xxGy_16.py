
def paths(x, y):
    if x * y == 0: return 1
    return paths(x-1, y) + paths(x, y-1)

