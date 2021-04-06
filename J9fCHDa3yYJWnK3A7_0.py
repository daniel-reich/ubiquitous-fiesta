
def is_happy(n):
  if n == 4:
    return False
  elif n == 1:
    return True
  return is_happy(sum(int(i) ** 2 for i in str(n)))

