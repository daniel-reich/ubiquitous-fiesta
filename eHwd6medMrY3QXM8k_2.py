
def is_consecutive(s):
  for i in range(1, len(s)//2+1):
    currentn=int(s[:i])
    currenti=i
    direction=0
    while currenti<len(s):
      if ((direction==0 or direction==1) and len(s)-currenti>=len(str(currentn+1)) and s[currenti:currenti+len(str(currentn+1))]==str(currentn+1)):
        currentn+=1
        currenti+=len(str(currentn))
        direction=1
        if currenti==len(s):
          return True
      elif ((direction==0 or direction==2) and len(s)-currenti>=len(str(currentn-1)) and s[currenti:currenti+len(str(currentn-1))]==str(currentn-1)):
        currentn-=1
        currenti+=len(str(currentn))
        direction=2
        if currenti==len(s):
          return True
      else:
        break
  return False

