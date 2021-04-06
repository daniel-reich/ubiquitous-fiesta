
def not_good_math(n, k):
  while k:
    if n % 10:
      n -= 1
    else:
      n = int(str(n)[:-1])
    k -= 1
  return n

