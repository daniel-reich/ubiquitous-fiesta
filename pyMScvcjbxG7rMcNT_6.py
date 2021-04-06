
def sum_list(lst):
  s = 0
  for x in lst:
    s += sum_list(x) if type(x) == list else x
  return s

