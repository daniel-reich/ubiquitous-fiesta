
def canConcatenate(lst, target):
  for l in lst:
    for a in l:
      if a in target:
        target.remove(a)
      else:
        return False
  return len(target) == 0

