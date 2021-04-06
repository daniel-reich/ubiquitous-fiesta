
def sum_list(lst):
  if type(lst) == int:
    return lst
​
  total = 0
  for n in lst:
    total += sum_list(n)
  return total

