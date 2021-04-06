
def bound_sort(lst, bounds):
    if sorted(lst[:bounds[1]+1])+lst[bounds[1]+1:] == sorted(lst):
        return True
    else:
        return False

