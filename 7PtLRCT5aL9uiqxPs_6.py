
def last_dig(a, b, c):
  res = a % 10 * b % 10
  if res % 10 == c % 10:
    return True
  else:
    return False

