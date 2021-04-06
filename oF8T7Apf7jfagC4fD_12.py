
def antipodes_average(lst):
  a=len(lst)
  begLst=[]
  endLst=[]
  newLst=[]
  b=int(a/2)
  if(a%2==0):
    for i in range(0,b):
      begLst.append(lst[i])
    for i in range(b,a):
      endLst.append(lst[i])
  else:
    for i in range(0,b):
      begLst.append(lst[i])
    for i in range(b+1,a):
      endLst.append(lst[i])
  c=endLst[::-1]
  d=len(endLst)
  for i in range(0,d):
    newLst.append(float(begLst[i]+c[i])/2)
  return newLst

