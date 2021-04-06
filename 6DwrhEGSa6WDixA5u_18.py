
def is_narcissistic(n):
  l=len(str(n))
  return True if n==sum([int(x)**l for x in str(n) ]) else False

