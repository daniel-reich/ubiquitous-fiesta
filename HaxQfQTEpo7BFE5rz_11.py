
def alternate_pos_neg(lst):
  return 0 not in lst and all(a * b < 0 for a, b in zip(lst[:-1], lst[1:]))

