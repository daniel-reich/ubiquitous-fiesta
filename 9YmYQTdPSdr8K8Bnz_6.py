
def unique_lst(lst):
  positive_ints = []
  for value in lst:
    if value > 0 and value not in positive_ints:
      positive_ints.append(value)
  return positive_ints

