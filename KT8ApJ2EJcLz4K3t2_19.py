
def two_digit_sum(n):
  if n == 1:
    return 1
  else:
    res = 0
    while n != 0:
      res += n % 10
      n = int(n / 10)
    return res

