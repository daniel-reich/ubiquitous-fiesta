
def n_differences(lst):
  b = True
  while b:
      if len(lst) > 1:
        lst = [lst[i] - lst[i-1] for i in range(1, len(lst))]
      else:
        b = False
  for i in lst:
    return i

