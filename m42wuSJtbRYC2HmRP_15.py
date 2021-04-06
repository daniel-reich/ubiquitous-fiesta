
from math import log10
​
def largest_exponential(lst):
    maxi = (0, 0)
    for c, i in enumerate(lst):
        num = log10(i[0])*i[1]
        if num > maxi[1]:
            maxi = (c+1, num)
    return maxi[0]

