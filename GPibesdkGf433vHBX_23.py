
def goldbach_conjecture(n):
  p = 2
  while p<n:
    if isPrime(p) and isPrime(n-p): return [p,n-p]
    p+=1
  
def isPrime(n):
  for i in range(2,n):
    if n%i==0: return False
  return n>1

