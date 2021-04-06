
def is_narcissistic(n):
  n = str(n)
  return sum(int(i)**len(n) for i in n) == int(n)

