
def chocolates_parcel(n_small, n_big, order):
  s = n_small*2
  
  while n_big>=0:
    x = (order-(n_big*5))
    if s >= x and not x%2 and x>=0:
      return x//2
    n_big -= 1
  return -1

