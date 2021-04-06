
def setify(lst):
  temp = []
  for i in lst:
    if i not in temp:
      temp.append(i)
      
  return temp

