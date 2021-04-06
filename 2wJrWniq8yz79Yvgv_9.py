
def is_narcissistic(n):
  x = len(str(n))
  return n == sum(int(i)**x for i in str(n))

