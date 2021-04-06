
# https://edabit.com/challenge/qYrTDRY7AN2RHxvXg
​
import math
​
def f(a, h):
    x = h**4 - 16*a**2
    if x < 0:
        return "Does not exist"
​
    y = max((h**2 + math.sqrt(x))/2, (h**2 - math.sqrt(x))/2)
    s2 = math.sqrt(y)
    s1 = 2*a/s2
    l = [round(s1,3), round(s2,3)]
    l.sort()
    return l

