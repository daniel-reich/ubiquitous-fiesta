
import math
def largest_exponential(lst):
    res = [tpl[1] * math.log(tpl[0]) for tpl in lst]
    return res.index(max(res)) + 1

