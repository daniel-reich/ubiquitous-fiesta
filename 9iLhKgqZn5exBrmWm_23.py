
def ascending(n):
  length=1
  while(length<=len(n)//2):
    check=0
    for i in range(0,len(n),length):
      if(i!=0 and int(n[i:i+length])!=int(n[i-length:i])+1):
        check=1       
        length+=1
        break
    if(check==0):
      return True
  return False

