
def alternate_pos_neg(lst):
  a = all(i < 0 for i in lst[::2])
  b = all(j > 0 for j in lst[1::2])
  c = all(i > 0 for i in lst[::2])
  d = all(j < 0 for j in lst[1::2])
  return bool(a and b) or bool(c and d)

