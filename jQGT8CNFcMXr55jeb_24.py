
def numbers_sum(lst):
  sum = 0
  for thing in lst:
    if type(thing) == int:
      sum += thing
    else:
      continue
  return sum

