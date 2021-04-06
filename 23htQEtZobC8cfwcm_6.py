
def canConcatenate(lst, target):
  k = []
  for index in lst:
    k += index
  k.sort()
  target.sort()
  return k == target

