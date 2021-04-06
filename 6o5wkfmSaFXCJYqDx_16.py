
def abcmath(a, b, c):
  x = 0
  s = a
  while x < b:
    s = s + s
    x = x + 1
  dm = divmod(s, c)   
  if dm[1] == 0:
    return True
  else:
    return False

