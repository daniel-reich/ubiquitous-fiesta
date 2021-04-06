
def unique_lst(lst):
  positive_numbers = []
  for item in lst:
    if item > 0 and item not in positive_numbers:
      positive_numbers.append(item)
  return list(positive_numbers)

