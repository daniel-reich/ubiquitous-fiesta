
def has_factors(n):
  if n<2:
    return True
  if n == 2:
    return False
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return True
  return False
​
def primorial(n):
  p = []
  s = 2
  while len(p) < n:
    if not has_factors(s):
      p.append(s)
    s += 1
  output = 1
  for i in p:
    output *= i
  return output

