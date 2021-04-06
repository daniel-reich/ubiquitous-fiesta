
def diamond_arrays(x):
    lst1 = [[i] * i for i in range(1, x + 1)]
    lst2 = [[i] * i for i in range(x - 1, 0, -1)]
    return lst1 + lst2

