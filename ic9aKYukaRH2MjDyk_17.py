
def sort_by_last(txt):
  b=txt.split(" ")
  a=len(b)
  newLst=[]
  newStr=""
  for i in range(0,a):
    newLst.append(b[i])
  d=sorted(newLst, key=lambda x: x[len(x)-1])
  for i in range(0,a):
      if(i==0):
          newStr=newStr+d[i]
      else:
          newStr=newStr+" "+d[i]
  return newStr

