
def circular_shift(lst1, lst2, n):
  return lst1[n:] + lst1[:n] == lst2

