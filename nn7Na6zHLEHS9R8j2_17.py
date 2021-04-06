
def deep_count(lst):
  return len(lst) + sum([(deep_count(i) if isinstance(i, list) else 0) for i in lst])

