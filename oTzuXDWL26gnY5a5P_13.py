
from functools import reduce
​
def prime_numbers(num):
  numOfPrime = 0
  for a in range (1, num + 1):
    if factors(a):
      numOfPrime += 1
  return numOfPrime
      
​
def factors(n):
  return len(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))) == 2

