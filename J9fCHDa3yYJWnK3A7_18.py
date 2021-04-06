
def is_happy(n):
  return True if s(n) == 1 else False if s(n) == 4 else is_happy(s(n))
def s(n):
  return sum([int(x)**2 for x in str(n)])

