
from math import log
​
​
def largest_exponential(lst):
    return lst.index(max(lst, key=lambda num: num[1]*log(num[0]))) + 1

