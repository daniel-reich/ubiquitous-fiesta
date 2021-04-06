
def anti_divisors(n):
  newLst=[]
  for i in range(2,n):
    if(n%i!=0):
      if(i%2!=0):
        if((n*2-1)%i==0 or (n*2+1)%i==0):
          newLst.append(i)
      else:
        if((n*2)%i==0):
          newLst.append(i)
  return newLst

