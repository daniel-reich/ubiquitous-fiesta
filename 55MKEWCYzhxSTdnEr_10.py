
def gcd(a, b):
  small = a if a < b else b
  large = b if b > a else a
  i = small
  while i > 0:
    if small % i == 0 and large % i == 0:
      return i
    i -= 1
  return 1

