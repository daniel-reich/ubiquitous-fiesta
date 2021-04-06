
def clear_ordering(lst):
    d = {x:y for x,y in lst}
    return sum([1 for y in d.values() if y in d]) == len(lst) - 1

