
def less_or_equal(lst, k):
  lst.sort()
  if k == 0:
    if lst==[1]:
      return None
    return 1
  if len(lst) == k:
    return lst[k-1]
  if lst[k] == lst[k-1]:
    return None
  return lst[k-1]

