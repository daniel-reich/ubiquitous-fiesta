
def primes_below_num(n):
  l=[]
  for i in range(2,n+1):
    for j in range(2,i):
      if i%j==0:
        break
    else:
      l.append(i) 
  return l

