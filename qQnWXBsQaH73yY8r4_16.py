
def factor(n):
  if n == 1: return 1
  return n*factor(n-1)
  
def isFact(n):
  return [i for i in range(2,n) if n%i == 0]
​
def kempner(n):
  elst = []
  x = isFact(n) 
  if len(x)>1:
    for i in x:
      if factor(i)%n ==0: elst.append(i)
  return min(elst) if len(elst)>0 else n
  return n

