
def makeSandwich(i,f):
  a=len(i)
  newLst=[]
  for j in range(0,a):
    if(i[j]==f):
      newLst.append("bread")
      newLst.append(i[j])
      newLst.append("bread")
    else:
      newLst.append(i[j])
  return newLst

