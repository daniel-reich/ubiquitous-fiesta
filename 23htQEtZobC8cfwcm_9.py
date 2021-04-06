
def canConcatenate(lst, target):
  return sorted(item for sublist in lst for item in sublist) == sorted(target)

