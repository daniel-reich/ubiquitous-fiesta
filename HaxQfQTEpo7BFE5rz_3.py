
def alternate_pos_neg(lst):
  if 0 in lst:
    return False
  return all(a*b < 0 for a, b in zip(lst, lst[1:]))

