
import collections
def circular_shift(lst1, lst2, n):
  a=collections.deque(lst1)
  a.rotate(n)
  return list(a)==lst2

