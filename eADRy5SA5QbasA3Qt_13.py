
def is_harshad(n):
  x = 0
  y = str(n)
  for i in y:
    x += int(i)
  if n%x == 0:
    return True
  else:
    return False

