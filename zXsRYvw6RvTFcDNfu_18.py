
def ruth_aaron(n):
  for i in [n-1,n+1]:
    res=0
    if sum(set(primef(n)))==sum(set(primef(i))):res+=1
    if sum(primef(n))==sum(primef(i)):res+=2
    if res!=0:return ['Aaron',res] if i<n else ['Ruth',res] 
  return False
  
def primef(num):
  res=[];i=2
  while num!=1:
    if not num%i:
      res+=[i]
      num//=i
    else:i+=1
  return res

