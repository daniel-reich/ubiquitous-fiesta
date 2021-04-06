
def sum_of_holes(n):
    d, holes = {'0': 1, '4': 1, '6': 1, '8': 2, '9': 1}, 0
    for i in range(4, n + 1):
        holes += sum(d.get(c, 0) for c in str(i))
    return holes

