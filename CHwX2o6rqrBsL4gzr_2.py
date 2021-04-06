
def check_title(txt):
  for x in txt.split():
    if x[0] != x[0].upper():
      return False
  return True

