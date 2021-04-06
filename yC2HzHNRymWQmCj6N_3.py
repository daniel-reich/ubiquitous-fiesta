
def less_or_equal(lst, k):
  for x in lst:
    if k:
      if sum(y<=x for y in lst)==k:
        return x
    else:
      if lst==[1]:
        return None
      else:
        return 1
  return None

