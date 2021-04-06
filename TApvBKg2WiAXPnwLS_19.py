
def nth_smallest(lst,num):
    if num > len(lst):
        return None
    else:
        return sorted(lst)[num-1]

