
def diamond_arrays(x):
    lst = list(range(1,x)) + list(range(x,0, -1))
    return [[x]* x for x in lst]

