
def find_vertex(a, b, c):
  x = -0.5 * b / a
  y = a*x**2 + b*x + c
  return [x, y]

