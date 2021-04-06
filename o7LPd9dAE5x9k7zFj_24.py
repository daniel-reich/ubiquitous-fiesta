
import math
​
def logarithm(base, num):
​
    if (base > 0) and (base != 1) and (num > 0):
        outcome = math.log(num, base)
        return outcome
​
    return "Invalid"

