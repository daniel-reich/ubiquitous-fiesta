
def deep_count(lst):
  count = 0
  if not isinstance(lst, list):
    return 1
  for item in lst:
    count = count + 1
    if isinstance(item, list):
      count = count + deep_count(item)
  return count

