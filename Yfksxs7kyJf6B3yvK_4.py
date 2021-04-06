
def min_miss_pos(lst):
    return min(set(range(1, max(lst)+2))-set(lst))

