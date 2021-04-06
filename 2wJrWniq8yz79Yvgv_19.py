
def is_narcissistic(n):
  return n == sum([int(x) ** len(str(n)) for x in str(n)])

