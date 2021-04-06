
def canConcatenate(lst, target):
  return sorted([i for j in lst for i in j]) == sorted(target)

