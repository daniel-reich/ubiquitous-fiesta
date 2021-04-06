
def circular_shift(lst1, lst2, n):
  if n<0:
    while n<0:
      lst1 = lst1[-1:] + lst1[:-1]
      n = n+1
  elif n>0:
    while n>0:
      lst1 = lst1[1:] + lst1[:1]
      n = n-1
  return lst1==lst2

