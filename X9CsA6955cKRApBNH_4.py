
from itertools import accumulate
def longest_run(lst):
    def longest_r(lst_):
        ones = [1 if b==a+1 else 0 for a,b in zip(lst_, lst_[1:])]
        runs = max(accumulate([0]+ones, lambda x,y: (x+y)*y if (x+y)*y != 1 else 2))
        return runs or 1
    return max(longest_r(lst), longest_r(lst[::-1]))

