
import math
def largest_exponential(lst):
    return max([(y*math.log(x), i+1)
             for i, (x, y) in enumerate(lst)])[1]

