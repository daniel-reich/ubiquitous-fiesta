
def canConcatenate(lst, target):
  return len([num for sub in lst for num in sub]) == len(target)

