
def remove_smallest(lst):
    if not lst: return []
    lst.remove(min(lst))
    return lst

