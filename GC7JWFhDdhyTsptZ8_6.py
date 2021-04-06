
#This isn't very efficient lol
def isPrime(n):
  for i in range(2,n//2):
    if (n%i)==0: return False
  return True
​
def sexy_primes(n, limit):
  sexyPrimes = []
  for i in range(2,limit-n):
    is_prime = isPrime(i)
    if is_prime:
      lst,appnd = [i], True
      for j in range(1,n):
        if isPrime(i+(j*6)) == True and (i+(j*6)<limit): lst.append(i+(j*6))
        else:
          appnd=False
          break
      if appnd: sexyPrimes.append(tuple(lst))
  return sexyPrimes

