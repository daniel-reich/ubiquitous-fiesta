
def is_happy(n):
  if n==1:
    return True
  elif n==4:
    return False
  else:
    return is_happy(sum(int(x)**2 for x in str(n)))

