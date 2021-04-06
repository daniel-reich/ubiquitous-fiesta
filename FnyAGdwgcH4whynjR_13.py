
import itertools
def get_subsets(lst, n):
    r = []
    for x in range(1, len(lst) + 1):
        i = itertools.combinations(lst, x)
        r += [list(x) for x in i if sum(x) == n]
    return sorted(r, key=lambda x : (len(x), x[0]))

