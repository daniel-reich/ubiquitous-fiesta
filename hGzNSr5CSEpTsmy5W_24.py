
def not_good_math(n, k):
  for _ in range(k):
    if n % 10 == 0:
      n = n // 10
    else:
      n = n - 1
  return n

