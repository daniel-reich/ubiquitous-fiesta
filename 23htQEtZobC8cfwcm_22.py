
def canConcatenate(lst, target):
  r = []
  for l in lst:
    r += l
  return all(r.count(e) == target.count(e) for e in target)

