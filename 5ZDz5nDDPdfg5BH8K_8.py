
def only_5_and_3(n):
  if n % 5 == 0: return True
  elif n == 51:
    return False
  for i in range(n//3):
    if (n - (3*i)) % 5 == 0: return True
  return False

