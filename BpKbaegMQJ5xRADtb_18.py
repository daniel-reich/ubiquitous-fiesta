
def isprime(n):
  if n == 0 or n == 1: return False
  for i in range(2,n):
    if n%i == 0:
      return False
  return True
​
def is_unprimeable(num):
  if isprime(num): return "Prime Input"
  num_s = str(num)
  primes = []
  for i in range(len(num_s)):
    for j in range(10):
      check = ""
      for k in range(len(num_s)):
        check += num_s[k] if k != i else str(j)
      if isprime(int(check)):
        primes.append(int(check))
  return "Unprimeable" if len(primes) == 0 else sorted(primes)

