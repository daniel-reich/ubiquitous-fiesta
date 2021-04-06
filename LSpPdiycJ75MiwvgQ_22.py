
import math
​
def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))
​
def grid_pos(lst):
    n, m = lst
    return binomial_coefficient(n + m, n)

