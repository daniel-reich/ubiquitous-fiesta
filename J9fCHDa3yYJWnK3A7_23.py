
def is_happy(n):
  s = sum([int(i)**2 for i in str(n)])
  if s == 1:
    return True
  elif s == 4:
    return False
  else:
    return is_happy(s)

