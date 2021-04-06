
def iso_group(lst,m=-1000000000000,l=[],index=0):
  if(index>=len(lst)):
    if(len(l)==1):
      return l[0]
    else:
      return l
  elif(lst[index]>m):
    m=lst[index]
    l=[m]
  elif(lst[index]==m):
    l.append(m)
    
  return iso_group(lst,m,l,index+1)

