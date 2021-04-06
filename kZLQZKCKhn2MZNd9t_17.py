
def possible_bonus(a, b):
  if a >= b:
    return False
  elif b >= a + 7:
    return False
  elif 6 < a - b:
    return False
  else:
    return True

