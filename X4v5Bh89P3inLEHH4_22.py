
def spin_around(lst):
    d = {'right': 1, 'left': -1}
    return abs(sum(d[x] for x in lst)) * 90 // 360

