
def chocolates_parcel(n_small, n_big, order):
  for i in range(0,n_small+1):
    for j in range(0,n_big+1):
      if i*2 + j*5 == order:
        return i
  return -1

