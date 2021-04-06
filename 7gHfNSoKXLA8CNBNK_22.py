
def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)
​
​
def sim_prop_frac(max_den):
  counter = 0
  for denominator in range(2, max_den + 1):
    for numerator in range(1, denominator):
      if gcd(denominator, numerator) == 1:
        counter += 1
  return counter

