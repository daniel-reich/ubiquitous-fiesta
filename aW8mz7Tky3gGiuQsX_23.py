
def factors(n):
  output = []
  for i in range(1, n+1):
    if n % i == 0:
      output.append(i)
  return output
​
def is_prime(n):
  if n == 1:
    return False
  if n == 2:
    return True
  for i in range(2,int(n**0.5)+1):
    if n%i == 0:
      return False
  return True
​
def is_powerful(n):
  prime_factors = [i for i in factors(n) if is_prime(i)]
  for i in prime_factors:
    if i**2 not in factors(n):
      return False
  return True

