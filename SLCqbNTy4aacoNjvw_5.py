
def remove_dups(lst):
    unique = set()
    return [x for x in lst if not (x in unique or unique.add(x))]

