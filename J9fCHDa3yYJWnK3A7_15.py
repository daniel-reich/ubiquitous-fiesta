
def is_happy(n):
  if n==1:
    return True
  elif n==4:
    return False
  return is_happy(sum([int(i)**2 for i in str(n)]))

