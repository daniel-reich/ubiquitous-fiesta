
from itertools import combinations
def get_subsets(lst, n):
    return [ list(s) for l in range(len(lst)+1) for s in combinations(lst, l) if sum(s) == n]

