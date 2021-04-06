
def is_symmetrical(num):
  if list(reversed(str(num)))==list(str(num)):
    return True
  else:
    return False

