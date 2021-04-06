
from itertools import groupby
from operator import itemgetter
​
def final_countdown(lst):
    groups = [list(map(itemgetter(1), g)) for k, g in groupby(enumerate(lst), lambda x: x[0]+x[1])]
    count_downs = [g for g in groups if g[-1] == 1]
    return [len(count_downs), count_downs]

