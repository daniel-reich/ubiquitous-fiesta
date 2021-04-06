
def has_spaces(txt):
  x = txt.split(" ")
  x = len(x)
  if x == 1:
    return False
  elif x > 1:
    return True

