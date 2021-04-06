
def deep_count(lst):
  count = 0
  for v in lst:
    if isinstance(v, list):
      count += deep_count(v)
    count += 1
  return count

