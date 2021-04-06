
def count_number(lst):
  count = 0
  for l in lst:
    if type(l) is list:
      count += count_number(l)
    elif type(l) is float or type(l) is int:
      count += 1
  return count

