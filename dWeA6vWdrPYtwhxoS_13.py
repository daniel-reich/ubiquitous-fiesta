
def count_number(lst):
  count = 0
  for i in lst:
    if isinstance(i, list):
      count += count_number(i)
    else:
      if isinstance(i, (int, float, complex)) and not isinstance(i, bool):
        count += 1
  return count

