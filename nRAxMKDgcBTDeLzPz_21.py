
def circular_shift(lst1, lst2, n):
  i = n%len(lst1)
  return lst1 == lst2[i:]+lst2[:i]

