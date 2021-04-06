
def can_complete(initial, word):
  tempw = [x for x in word]
  tempi = [x for x in initial]
  index = []
  for i in range(len(tempi)):
    if tempi[i] in tempw:
      index.append(tempw.index(tempi[i]))
      tempw.remove(tempi[i])
    else:
      return False
  print(index)
  if index == sorted(index):
    return True
  return False

