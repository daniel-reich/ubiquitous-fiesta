
import itertools
def three_sum(lst):
    return sorted([list(i) for i in set(itertools.combinations(lst,3)) if sum(i) == 0],key=lambda x: lst.index(x[0]))

