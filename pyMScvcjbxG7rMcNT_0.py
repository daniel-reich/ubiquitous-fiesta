
def sum_list(lst):
  s = 0
  for x in lst:
    if type(x) == int:
      s = s + x
    else:
      s = s + sum_list(x)
  return s

