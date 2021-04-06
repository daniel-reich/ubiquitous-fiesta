
def find_missing(lst):
  if not lst or any(not i for i in lst):
    return False
  sort = sorted(len(i) for i in lst)
  return next(i-1 for idx, i in enumerate(sort[1:]) if sort[idx] != i-1)

