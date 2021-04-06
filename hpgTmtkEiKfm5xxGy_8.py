
def paths(x, y):
    if x == 0 and y == 0:
        return 1
    elif x == 0 and y > 0:
        return paths(x, y - 1)
    elif x > 0 and y == 0:
        return paths(x - 1, y)
    else:
        return paths(x - 1, y) + paths(x, y - 1)

