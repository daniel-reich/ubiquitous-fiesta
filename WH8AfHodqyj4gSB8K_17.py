
from collections import Counter
def is_authentic_skewer(n):
  v=["A","E","I","O","U"]
  z=n.replace("-","")
  if(len(z)<2):
    return False
  i=0
  step=list()
  c=0
  i=0
  while(i<len(n)):
    if((i==0 or i==len(n)-1) and n[i] in v):
      return False
    elif(n[i]=='-'):
      j=i
      while(j<len(n) and n[j]=='-'):
        j+=1
      step.append(j-i)
      i=j   
    elif(c==0 and n[i] not in v):
      c=1
      i+=1
    elif(c==1 and n[i] in v):
      c=0
      i+=1
    elif(c==0 and n[i] in v):
      return False
    elif(c==1 and n[i] not in v):
      return False
  if(len(Counter(step))!=1):
    return False
  return True

