
def alternate_pos_neg(lst):
  if len(lst) == 1:
    return lst[0] != 0
  for i in range(len(lst) - 1):
    if lst[i] * lst[i+1] >= 0:
      return False
  return True

