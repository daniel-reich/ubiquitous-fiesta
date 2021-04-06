
def is_narcissistic(n):
  return sum([int(x)**len(str(n)) for x in list(str(n))])==n

