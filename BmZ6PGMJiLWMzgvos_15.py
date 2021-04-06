
def is_special_array(lst):
  for i in range(len(lst)):
    if (i % 2 == 0) and (lst[i] % 2 == 1): return False
    if (i % 2 == 1) and (lst[i] % 2 == 0): return False
  return True

