
from math import factorial
def formula(n, k):
    return factorial(n) // (factorial(n - k) * factorial(k))
def pascals_triangle(n):
    return [formula(n, k) for n in range(n) for k in range(n + 1)]

