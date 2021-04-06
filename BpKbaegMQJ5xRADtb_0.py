
def is_unprimeable(num):
  if is_prime(num):
    return 'Prime Input'
​
  primes = []
  for i in range(len(str(num))):
    for d in range(10):
      m = replace_digit(num,d,i)
      if is_prime(m):
        primes.append(m)
  return sorted(primes) or 'Unprimeable'
  
def is_prime(n):
  return n > 1 and all(n%i for i in range(2,int(n**0.5)+1))
​
def replace_digit(n,d,i):
  return int(str(n)[:i] + str(d) + str(n)[i+1:])

