
def deep_count(lst):
  count = 0
  for l in lst:
    count += deep_count(l)+1 if isinstance(l, list) else 1
  return count

