
def prime(n):
  a=[]
  for i in range(1,n+1):
    if n%i==0:
      a.append(i)
  return len(a)==2
def eratosthenes(num):
  x=[]
  for i in range(2,num+1):
    if prime(i):
      x.append(i)
  return x

