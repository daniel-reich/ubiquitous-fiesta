
def can_traverse(x):
  oldLst = x[0][0:4]
  for j in range(1, len(x[0])):
    newLst = [i[j] for i in x]
    if (abs(newLst.count(1) - oldLst.count(1)) > 1):
      return(False)
    oldLst = newLst
  return(True)

