
def abcmath(a, b, c):
  for i in range(b):
    a += a
  
  if a % c == 0:
    return True
  else:
    return False

