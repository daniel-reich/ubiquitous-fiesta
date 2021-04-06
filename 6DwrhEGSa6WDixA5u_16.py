
def is_narcissistic(n):
  return True if sum([int(i)**len(str(n)) for i in str(n)]) == n else False

