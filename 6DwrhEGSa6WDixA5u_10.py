
def is_narcissistic(n):
  n = str(n)
  return sum([int(x)**len(n) for x in n]) == int(n)

