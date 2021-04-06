
def esthetic(num):
  lst = []
  for i in range(2,11):
    temp = base(num,i)
    if all([abs(temp[i]-temp[i+1])==1 for i in range(len(temp)-1)]):
      lst.append(i)
  return lst if lst else "Anti-Esthetic"
  
def base(n,b):
  blst = list(range(b))
  lst = []
  while n>0:
    lst.append(blst[n%b])
    n=n//b
  return lst[::-1]

