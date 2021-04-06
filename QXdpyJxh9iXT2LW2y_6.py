
import math
def check(n):
  if n == 1: 
    return False
  if n == 2: 
    return True
  pri = True
  for i in range(2, n): 
    if n%i == 0: 
      pri = False
  return pri
​
def product_of_primes(num):
  if check(num): 
    return False
  l = []
  for i in range(2, num): 
    if num%i == 0:
      l.append(i)
  if all(check(i)for i in l): 
    return True
  else: 
    return False
def square(h): 
  if round(math.sqrt(h))**2 == h: 
    return True
  else: 
    return False
def semiprimes(n):
  l = []
  for i in range(2, n): 
    if product_of_primes(i): 
      l.append(i)
  ll = []
  for i in l: 
    if not square(i): 
      ll.append(i)
  return (l, ll)

