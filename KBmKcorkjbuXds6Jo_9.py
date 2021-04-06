
def chocolates_parcel(n_small, n_big, order):
  def possible(small, big, order):
    if order % 5 == 0:
      return order // 5 <= big
    elif small == 0 or order < 0:
      return False
    else:
      return possible(small - 1, big, order - 2)
  def count_smallest(order):
    if order % 5 == 0:
      return 0
    else:
      return 1 + count_smallest(order - 2)
  
  poss = possible(n_small, n_big, order)
​
  if poss == True:
    return count_smallest(order)
  else:
    return -1

