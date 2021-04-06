
def count(n):
  k = 0
  if n == 0:
    return 1
  if n < 0:
    n *= -1
  while n > 0:
    n = int(n / 10)
    k +=1
  return k

