
def spin_around(lst):
    return abs(sum(1 if d == 'right' else -1 for d in lst))//4

