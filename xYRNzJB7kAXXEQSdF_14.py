
def wiggle_string(s):
  a=len(s)
  newStr=""
  newLst=[]
  for i in range(0,a):
    newStr=s.rjust(a+i," ")
    newLst.append(newStr)
  for i in range(a,-1,-1):
    newStr=s.rjust(a+i," ")
    newLst.append(newStr)
  return newLst

