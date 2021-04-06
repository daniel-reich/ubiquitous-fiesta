
def canConcatenate(lst, target):
  lst=[lists for sublist in lst for lists in sublist]
  return sorted(lst)==sorted(target)

