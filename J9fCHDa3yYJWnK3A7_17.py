
def f(n):
  return sum(int(d)**2 for d in str(n))
def is_happy(n):
  return True if n == 1 else False if n == 4 else is_happy(f(n))

