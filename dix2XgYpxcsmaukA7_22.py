
def getprime(n):
  if n%2==0: return 2
  for i in range(3,n,2):
    if n%i==0:return i
  return n
​
  
def express_factors(n):
  m=n
  print(m)
  lst=[]
  while m>1:
    tmp=getprime(m)
    lst.append(tmp)
    m=m//tmp
  out=[]
  data=list(set(lst))
  data.sort()
  for x in data:
    tmp=lst.count(x)
    out.append(str(x) + ("^"+str(tmp) if tmp>1 else ''))
​
  return ' x ' .join(out)

