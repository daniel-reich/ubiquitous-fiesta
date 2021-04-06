
def count_number(lst):
  n = 0
  for i in lst:
    if isinstance(i, (int, float)):
      n += 1
    elif isinstance(i, list):
      n += count_number(i)
  return n

