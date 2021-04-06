
import math
​
# ln(x^y) = y * ln(x)
​
def largest_exponential(lst):
    largest = 0
    for i in range(len(lst)):
        x, y = lst[i]
        val = y * math.log(x)
        if val > largest:
            largest = val
            ans = i + 1
    return ans

