
def max_possible(a, b):
  bestResult = ""
  strA, strB = str(a), str(b)
  useB = False
  for i in strA:
    currentHighest = int(i)
    for j in strB:
      if currentHighest < int(j):
        currentHighest = int(j)
        useB = True
    bestResult += str(currentHighest)
    if useB:
      useB = False
      strB = strB.replace(str(currentHighest), "", 1)
  return int(bestResult)

