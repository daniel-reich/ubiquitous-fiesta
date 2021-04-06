
def covered_integers(lst):
    lst = [list(range(sublist[0], sublist[1]+1)) for sublist in lst]
    return len(set([i for sublist in lst for i in sublist]))

