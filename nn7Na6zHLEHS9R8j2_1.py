
def deep_count(lst):
  if not type(lst) == list: return 0
  count = len(lst)
  for el in lst:
    count += deep_count(el)
  return count

