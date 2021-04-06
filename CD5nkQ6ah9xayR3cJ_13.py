
def add_odd_to_n(n):
  res = 0
  if n == 1:
    res = n
  else:
    for i in range(1, n+1):
      if i % 2 != 0:
        res += i
  return res

