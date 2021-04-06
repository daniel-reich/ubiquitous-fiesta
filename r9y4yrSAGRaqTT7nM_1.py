
def find_missing(lst):
  if not lst or any(i in (None, []) for i in lst):
    return False
  arr = set(len(i) for i in lst)
  missing = set(range(min(arr), max(arr) + 1)) - arr
  return missing.pop()

