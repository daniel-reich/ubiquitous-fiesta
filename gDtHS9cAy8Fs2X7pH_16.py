
def count_repetitions(lst):
  myDict = {}
  for item in lst:
    if item not in myDict:
      myDict[item] = 1
    else:
      myDict[item] += 1
  return myDict

