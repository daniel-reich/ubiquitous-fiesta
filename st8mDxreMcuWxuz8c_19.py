
def pentagonal(num):
  n = 1
  while num > 1:
    n = n + 5 * (num - 1)
    num -= 1
  return n

