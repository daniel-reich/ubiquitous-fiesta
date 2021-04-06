
def count_boomerangs(lst):
    return sum(1 for a,b,c in zip(lst, lst[1:], lst[2:]) if a == c != b)

