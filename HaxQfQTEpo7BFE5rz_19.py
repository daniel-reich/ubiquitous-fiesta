
def alternate_pos_neg(lst):
  if all(x > 0 for x in lst[0::2]):
    return all(x < 0 for x in lst[1::2])
  elif all(x < 0 for x in lst[0::2]):
    return all(x > 0 for x in lst[1::2])
  else:
    return False

