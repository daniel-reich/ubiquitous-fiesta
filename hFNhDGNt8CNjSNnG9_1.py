
def setify(lst):
  setlst = []
  
  for i in lst:
    if i not in setlst: setlst.append(i)
  
  return setlst

