
def count_number(lst):
  s = 0
  for el in lst:
    if type(el) in (int, float):
      s += 1
    elif type(el) == list:
      s += count_number(el)
  return s

