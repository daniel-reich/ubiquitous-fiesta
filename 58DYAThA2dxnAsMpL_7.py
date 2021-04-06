
def integer_boolean(n):
  outputList = []
  numList = [int(x) for x in str(n)]
  for i in numList:
    if i == 1:
      outputList.append(True)
    else:
      outputList.append(False)
  return outputList

