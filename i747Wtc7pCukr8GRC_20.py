
import itertools
import numpy as np
​
def max_product(lst):
    perm = list(itertools.permutations(lst, 3))
    all_prods = [np.prod(i) for i in perm]
    return max(all_prods)
​
def min_product(lst):
    perm = list(itertools.permutations(lst, 3))
    all_prods = [np.prod(i) for i in perm]
    return min(all_prods)

