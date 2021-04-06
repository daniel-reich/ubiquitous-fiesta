
def covered_integers(lst):
    lst_new = []
    ([[lst_new.append(b) for b in range(a[0], a[1]+1)] for a in lst])
    return len(set(lst_new))

