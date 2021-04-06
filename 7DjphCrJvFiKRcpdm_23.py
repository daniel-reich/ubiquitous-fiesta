
def covered_integers(lst):
    b = []
    for i in lst:
        b.extend(list(range(i[0], i[1]+1)))
    return len(set(b))

