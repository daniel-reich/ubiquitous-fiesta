
def not_good_math(n, k):
  for m in range(k):
    if not n % 10:
      n = n // 10
    else:
      n -= 1
  return n

