
def sum_missing_numbers(lst):
  r = 0
  lst2 = sorted(lst)
  for i in range(lst2[0], lst2[-1], 1):
    if i not in lst:
      r+=i
  return r

