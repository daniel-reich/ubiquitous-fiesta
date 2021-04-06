
def is_triangle(a, b, c):
  if a  + b  > c:
    if b + c > a:
      if a + c > b:
        return True
  return False

