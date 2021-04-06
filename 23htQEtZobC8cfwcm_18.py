
def canConcatenate(lst, target):
  lst = [ item for inner in lst for item in inner]
  return sorted(lst) == sorted(target)

