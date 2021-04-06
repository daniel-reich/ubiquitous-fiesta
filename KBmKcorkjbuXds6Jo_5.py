
def chocolates_parcel(n_small, n_big, order):
  fives = order // 5
  if fives > n_big:
    left = order - n_big * 5
  else:
    left = order % 5  
  if left % 2:
    left += 5 
  if left / 2 <= n_small:
    return left / 2 
  else:
    return -1

