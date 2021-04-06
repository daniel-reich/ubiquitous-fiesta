
def alternate_pos_neg(lst):
  return all(n>0 for n in lst[::2]) and all(n<0 for n in lst[1::2]) or all(n<0 for n in lst[::2]) and all(n>0 for n in lst[1::2])

