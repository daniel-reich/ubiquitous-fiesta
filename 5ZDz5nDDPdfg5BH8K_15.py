
def only_5_and_3(n):
  if n<0:
    return False
  elif n ==51:
    return False
  if n%5 == 0 or n%3==0:
    return True
  
  else:
    return only_5_and_3(n-5)

