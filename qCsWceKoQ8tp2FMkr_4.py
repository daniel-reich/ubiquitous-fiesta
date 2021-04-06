
def is_triangle(a, b, c):
  sides = sorted([a,b,c])
  return sides[2] < sides[0] + sides[1]

