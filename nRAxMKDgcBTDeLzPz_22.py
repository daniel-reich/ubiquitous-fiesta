
from collections import deque
​
​
def circular_shift(lst1, lst2, n):
    shifted = deque(lst1)
    shifted.rotate(n)
    return list(shifted) == lst2

