
def alternate_pos_neg(lst):
  if 0 in lst:
    return False
  for i in range(len(lst)-1):
    if lst[i] > 0:
      if lst[i+1] > 0:
        return False
    else:
      if lst[i+1] < 0:
        return False
  return True

