
def is_narcissistic(n):
  return n == sum([int(i) ** len(str(n)) for i in str(n)])

