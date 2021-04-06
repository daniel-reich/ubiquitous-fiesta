
from math import floor
​
def is_heteromecic(n):
    if n % 2 != 0:
        return False
    else:
        return floor(n ** 0.5) * (floor(n ** 0.5) + 1) == n

