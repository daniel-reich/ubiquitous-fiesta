
def gcd(a, b):
  divs = []
  for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
      divs.append(i)
  return max(divs)

