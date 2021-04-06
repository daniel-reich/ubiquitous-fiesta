
def primes_below_num(n):
  p=[]
  for i in range(2,n+1):
    if not [j for j in p if not i%j]:
      p.append(i)
  return p

