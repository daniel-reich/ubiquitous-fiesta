
from itertools import combinations
​
def three_sum(lst):
    return sorted((list(i) for i in set(combinations(lst, 3)) if sum(i) == 0), key = lambda x: lst.index(x[0]))

