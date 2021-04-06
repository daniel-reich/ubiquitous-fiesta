
def chocolates_parcel(n_small, n_big, order):
  countbig = 0
  countsmall = 0
  total = 0
  while(total < order-4 and countbig<n_big):
    countbig = countbig+1
    total = total+5
  if (order-total)%2 == 1:
    countbig = countbig-1
    total = total-5
  if(total==order):
      return countsmall
  while(countsmall<n_small):
    countsmall = countsmall+1
    total = total+2
    if(total==order):
      return countsmall
  return -1

