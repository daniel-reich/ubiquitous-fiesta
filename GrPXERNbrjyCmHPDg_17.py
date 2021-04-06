
def duplicate_count(txt):
  myDict = {}
  for c in txt:
    if c in myDict:
      myDict[c] += 1
    else:
      myDict[c] = 1
  sum = 0
  for v in myDict.values():
    if v > 1:
      sum += 1
  return sum

