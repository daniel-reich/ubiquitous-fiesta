
def gcd(n1, n2):
  for i in range(max(n1,n2), 0, -1):
    if n1 % i == 0 and n2 % i == 0:
      return i
    else:
      erg = i
  return erg

