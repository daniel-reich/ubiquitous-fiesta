
def sum_list(lst):
  total = 0
  for i in lst:
    if isinstance(i,list):
      total = total + sum_list(i)
    else:
      total = total + i
  return total

