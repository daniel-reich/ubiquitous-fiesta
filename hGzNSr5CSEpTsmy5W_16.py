
def not_good_math(n, k):
  counter = 0
  while counter < k:
    if str(n).endswith("0"):
      n = int(n / 10)
    else:
      n -= 1
    counter += 1
  return n

