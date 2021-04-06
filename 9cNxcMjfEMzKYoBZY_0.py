
def num_type(n):
  s = sum(factors(n))
  return 'Perfect' if s==n else 'Amicable' if sum(factors(s))==n else 'Neither'
​
def factors(n):
  return [i for i in range(1, (n//2) + 1) if not n%i]

