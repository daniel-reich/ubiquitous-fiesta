
def canConcatenate(lst, target):
  arr = []
  for row in lst:
    for elt in row:
      arr.append(elt)
  return sorted(arr)==sorted(target)

