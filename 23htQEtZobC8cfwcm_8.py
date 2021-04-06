
def canConcatenate(lst, target):
  return sorted(sum(lst,[])) == sorted(target)

