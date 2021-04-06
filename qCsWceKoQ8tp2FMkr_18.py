
def is_triangle(a, b, c):
  if a<0 and b<0 and c<0:
    return False
  elif a+b>c and a+c>b and b+c>a:
    return True
  else:
    return False

