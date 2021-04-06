
import functools 
def isprime(n):
  for i in range(2, n//2+1):
    if n % i == 0: return False
​
  return True
​
def mult(ls):
  return functools.reduce(lambda a, b: a * b, ls)
  
def primorial(n):
  ls = []
  num = 2
  
  while len(ls) < n:
    if isprime(num):
      ls.append(num)
    num += 1
  
  return mult(ls)

