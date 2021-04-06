
def landscape_type(lst):
  
  ans=''
  checkpeak=True
  checktrough=True
  index=1
  for (z,i) in enumerate(lst[1:-1]):
    checkpeak=True
    checktrough=True
    if lst[index-1]<i and lst[index+1]<i:
      for (x,j) in enumerate(lst[0:index]):
        if x !=0 and j<lst[x-1]:
          checkpeak=False
      x=index+1                    
      for (ab,j) in enumerate(lst[index+1:-1]):
        if x!=-1 and j<lst[x+1]:
          checkpeak=False
        x+=1                  
      if checkpeak==True:
        ans='mountain'
        break
    elif lst[index-1]>i and lst[index+1]>i:
      for (x,j) in enumerate(lst[0:index]):
        if x !=0 and j>lst[x-1]:
          checktrough=False
      x=index+1                    
      for (ab,j) in enumerate(lst[index+1:-1]):
        if x!=-1 and j>lst[x+1]:
          checktrough=False
        x+=1                    
      if checktrough==True:
        ans='valley'
        break   
    index+=1       
  if ans=='':
    ans='neither'
  return ans

