
def alternate_pos_neg(lst):
  if lst[0] == 0: return False
  if len(lst) == 1: return True
  for k in range(0, len(lst) - 2, 2):
    if lst[k] * lst[k + 1] >= 0:
      return False
  return lst[-1] * lst[-2] < 0

