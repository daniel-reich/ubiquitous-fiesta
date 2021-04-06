
def is_consecutive(s):
  
  for i in range(0,len(s)):
    increasing=0
    j=i+1
    n=int(s[:j])
    count=0
    while(j<len(s)):
      if(s[j:].startswith(str(n+1))):
        count=1
        j+=len(str(n+1))
        n+=1
        increasing=1
      elif(s[j:].startswith(str(n-1)) and increasing==0):
        count=1
        n-=1
        j+=len(str(n-1))
      else:
        count=0
        break
    if(count==1):
      return True
  return False

