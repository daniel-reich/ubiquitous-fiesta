
import math
def nespers(lst):
    ans = math.factorial(len(lst))
    for i in lst:
        if type(i) is list:
            ans *= nespers(i)
    return ans

