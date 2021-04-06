
def isPrime(n):
  if n==1:
    return False
  if n==2:
    return True
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True
def semiprimes(n):
  semisquare , seminot = [] , []
  for i in range(n+1):
    for d1 in range(2,int(i**0.5)+1):
      if i%d1==0:
        d2 = i//d1
        if d1!=d2 and isPrime(d1) and isPrime(d2):
          seminot.append(i)
        if isPrime(d1) and isPrime(d2):
          semisquare.append(i)
          break
  return semisquare, seminot

