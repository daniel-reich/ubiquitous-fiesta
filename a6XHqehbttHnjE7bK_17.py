
def is_repdigit(num):
  x = str(num).count(str(num)[0])
  y = len(str(num))
  return y == x

