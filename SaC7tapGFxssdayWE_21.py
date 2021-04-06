
def find_vertex(a, b, c):
  v = -b / (2 * a)
  return [v, a * v ** 2 + b * v + c]

