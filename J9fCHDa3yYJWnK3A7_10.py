
def is_happy(n):
  result = sum(int(x)**2 for x in str(n))
  if result == 4:
    return False
  elif result == 1:
    return True
  else:
    return is_happy(result)

