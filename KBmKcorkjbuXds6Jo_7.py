
def chocolates_parcel(n_small, n_big, order):
  for i in reversed(range(n_big+1)):
    cur = i*5
    small = n_small
    while cur+2<=order and small>0:
      cur+=2
      small-=1
    if cur==order:
      return n_small-small
  return -1

