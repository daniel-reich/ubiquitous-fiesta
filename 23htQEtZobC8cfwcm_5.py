
def canConcatenate(lst, target):
  return len([j for i in lst for j in i])==len(target)

