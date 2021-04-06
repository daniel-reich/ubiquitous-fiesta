
def prime(x):
  for n in range(2, int(x**.5) + 1):
    if x % n == 0: return False
  return True

