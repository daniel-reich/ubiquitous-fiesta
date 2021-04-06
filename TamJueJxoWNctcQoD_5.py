
def both(n1, n2):
  if n1 == 0 and n2 == 0:
    return True
  elif n1 < 0 and n2 < 0:
    return True
  elif n1 > 0 and n2 > 0:
    return True
  else:
    return False

