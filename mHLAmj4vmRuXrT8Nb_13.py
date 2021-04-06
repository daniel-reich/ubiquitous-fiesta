
def consecutive_combo(lst1, lst2):
  
  for i in range(len(lst2)):
    lst1.append(lst2[i])
  
  sortedList = sorted(lst1)
  a = []
  
  for i in range(len(sortedList) - 1):
    if sortedList[i + 1] - sortedList[i] == 1:
      a.append(1)
    else:
      a.append(0)
  
  return True if len(set(a)) == 1 else False

