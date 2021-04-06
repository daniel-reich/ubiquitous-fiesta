
prime = lambda num: len([n for n in range(2, num) if num % n == 0]) == 0
multipliers = lambda lst, index: lst[:index]
​
def primes(goal):
  prs = []
  n = 2
  while len(prs) < goal:
    if prime(n) == True:
      prs.append(n)
    n += 1
  return prs
​
def multiplier(multipliers):
  product = 1
  
  for multi in multipliers:
    product *= multi
  
  return product
  
primes = primes(9)
​
def primorial(n):
  
  m = multipliers(primes, n)
  return multiplier(m)

