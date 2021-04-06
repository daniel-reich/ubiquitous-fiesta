
def possible_bonus(a, b):
  if a>=b:
    return False
  else:
    if abs(a-b) <=6:
      return True
    return False

