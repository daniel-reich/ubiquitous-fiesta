
def chocolates_parcel(n_small, n_big, order):
  big = n_big * 5
  if big + n_small*2 < order:
    return -1
  while big > order:
    big -= 5
  for i in range(big,-1,-5):
    if not (order-i)%2:
      if (order-i)//2 <= n_small:
        return (order-i)//2
  return -1

