
from itertools import accumulate, combinations
def zero_indices(lst, k):
    def value(comb):
        lst_ = [1 if idx in comb else val for idx, val in enumerate(lst)]
        return max(accumulate(lst_, lambda x,y: y*x+y))
    zeros = (idx for idx, zero in enumerate(lst) if zero == 0)
    return list(max(combinations(zeros, k), key=value))

