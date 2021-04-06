
def nearest_element(n, lst):
    best = sorted(lst, key=lambda x: (-abs(x-n), x))[-1]
    return lst.index(best)

