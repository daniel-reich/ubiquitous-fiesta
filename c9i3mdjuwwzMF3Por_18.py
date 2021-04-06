
def bemirp(n):
  if not isPrime(n):
    return 'C'
  if isPrime(flip(n)) and flip(n)!=n :
    return 'B'
  elif isPrime(reverse(n)) and reverse(n)!=n:
    return 'E'
  elif isPrime(n):
    return 'P'
  
​
​
def isPrime(n):
  return len([x for x in range(1,n+1) if n%x==0])==2
​
def flip(n):
  key = {0:0,1:1,8:8,6:9,9:6}
  x = [int(y) for y in str(n)]
  if any([i not in key for i in x]):
    return False
  return int(''.join([str(key[i]) for i in x]))
  
def reverse(n):
  return int(str(n)[-1::-1])

