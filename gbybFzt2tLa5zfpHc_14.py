
import itertools
import collections
def three_sum(lst):
    perm = (itertools.combinations(lst, 3))
    fin_lst = list(collections.OrderedDict.fromkeys([i for i in perm if sum(i) == 0]))
    return [list(i) for i in fin_lst]

