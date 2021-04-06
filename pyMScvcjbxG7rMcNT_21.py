
def sum_list(lst):
  sum = 0
  for item in lst:
    sum += sum_list(item) if isinstance(item, list) else item
  return sum

