
def printgrid(rows, cols):
  ### initialize grid
  newlist = []
  newlist2 = []
  for i in range(rows):
    for i in range(cols):
      newlist2.append(i)
    newlist.append(newlist2)
    newlist2 = []
  iterator = 1
  for i in range(len(newlist[0])):
    for j in range(len(newlist)):
      newlist[j][i] = iterator
      iterator += 1
  return newlist

