
def not_good_math(n, k):
  for _ in range(k):
    if not n%10:
      n //= 10
    else:
      n -= 1
  return n

