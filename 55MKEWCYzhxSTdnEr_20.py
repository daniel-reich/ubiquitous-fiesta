
def gcd(a, b):
  if a < b:
    temp = a
    a = b
    b = temp
  if a % b == 0:
    return b
  else:
    return gcd(b,a%b)

