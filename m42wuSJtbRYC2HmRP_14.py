
import math
​
def largest_exponential(lst):
    l = [b*math.log(a) for (a,b) in lst]
    return l.index(max(l))+1

