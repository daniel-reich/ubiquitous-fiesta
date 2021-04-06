
def primefactors(n):
  factors, i = [], 2
  while n > 1:
    while not n%i:
      factors.append(i)
      n /= i
    i += 1
  return factors
​
def is_powerful(n):
  return all(not n % i**2 for i in primefactors(n))

