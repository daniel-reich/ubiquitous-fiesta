
def loves_me(n):
  returnList = []
  for i in range(n):
      if i % 2 == 0:
          returnList.append("Loves me")
      else:
          returnList.append("Loves me not")
  returnList[-1] = returnList[-1].upper()
  finalList = ', '.join(str(a) for a in returnList)
  return finalList

