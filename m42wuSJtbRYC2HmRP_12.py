
import math
def largest_exponential(lst):
    return (lambda x:x.index(max(x))+1)([i[1] * math.log(i[0]) for i in lst])

