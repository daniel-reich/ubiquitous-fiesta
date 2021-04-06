
def is_triangle(a, b, c):
  if a>b and a>c:
    if b+c>a:
      return True
  if b>a and b>c:
    if a+c>b:
      return True
  if c>b and c>a:
    if a+b>c:
      return True
  return False

