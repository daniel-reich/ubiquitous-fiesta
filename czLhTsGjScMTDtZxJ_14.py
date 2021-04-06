
primes=[2]
def primorial(n):
  a,product=1,1
  while len(primes)<n:
    lp=primes[-1]
    for i in range(lp+1+100*(a-1),lp+1+100*a):
      if all(i%p for p in primes):
        primes.append(i)
    if lp==primes[-1]:
      a+=1
    else:
      a=1
  for p in primes[:n]:
    product*=p
  return product

