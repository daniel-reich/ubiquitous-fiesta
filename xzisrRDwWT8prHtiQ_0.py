
def difference_two(lst):
    return sorted([a, b] for a in lst for b in lst if b - a == 2)

