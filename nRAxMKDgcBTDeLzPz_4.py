
def circular_shift(lst1, lst2, n):
  x = lst1[n:] + lst1[:n]
  return lst2 == x

