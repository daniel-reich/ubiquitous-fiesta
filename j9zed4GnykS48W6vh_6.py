
def digits(n):
  p10, ln, res = 10, 1, 0
  while p10 < n:
    res += ln*(p10 - p10//10)
    ln += 1
    p10 *=10
  return res + ln*(n - p10//10)

