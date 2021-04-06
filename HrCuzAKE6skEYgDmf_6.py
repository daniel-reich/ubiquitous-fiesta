
def pairs(lst):
  if len(lst) % 2 == 0:
    listI = []
    for i in range(0,(len(lst) // 2)):
      listA = []
      listA.append(lst[i])
      listA.append(lst[len(lst) - (i + 1)])
      listI.append(listA)
    return listI
  else:
    listI = []
    midpoint = (len(lst)/2) - 0.5
    for i in range(0,(len(lst) // 2)+1):
      listA = []
      if i == midpoint:
        listA.append(lst[i])
        listA.append(lst[i])
        listI.append(listA)
      else:
        listA.append(lst[i])
        listA.append(lst[len(lst) - (i + 1)])
        listI.append(listA)
    return listI

