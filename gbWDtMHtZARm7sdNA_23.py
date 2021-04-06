
def And(a, b):
  if a is True and b is True:
    return True
  elif a is True and b is False or b is True and a is False:
    return False
  else:
    if a is False and b is False:
      return False

