
def consecutive_sum(n):
  i, res = 2, 0
  while 2 ** i <= n:
    res = 2 ** i
    i += 1
  return res != n

