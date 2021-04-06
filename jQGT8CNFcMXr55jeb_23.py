
def numbers_sum(lst):
  start = 0
  for x in lst:
    if type(x) is int:
      start = start + x
    else:
      continue
  return start

