
def isPrime(n):
  i = 2
  tallies = 0
  while n > i:
    if n%i == 0:
      tallies += 1
    i += 1
  return(tallies==0)
​
def next_prime(num):
  if isPrime(num):
    return num
  else:
    return next_prime(num+1)

