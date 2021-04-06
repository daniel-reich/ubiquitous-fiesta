
def is_narcissistic(n):
  pow = len(str(n))
  return sum([int(i)**pow for i in str(n)]) == n

