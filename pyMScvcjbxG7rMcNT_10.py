
def sum_list(lst):
  total = 0
  for i in lst:
    if type(i) is int:
      total += i
    else:
      total += sum_list(i)
  return total

