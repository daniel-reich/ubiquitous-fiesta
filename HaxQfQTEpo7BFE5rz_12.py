
def alternate_pos_neg(lst):
  i = 0
  k = 0
  if lst.count(0):
    return False
  while i < len(lst):
    if lst[i] < 0:
      k += 1
    i += 1
    if i == len(lst):
      break
    if lst[i] > 0:
      k += 1
    i += 1
  return k == 0 or k == len(lst)

