
def find_vertex(a, b, c):
  x = round(-(b/(2*a)),2)
  y = round(a*x*x + b*x + c,2)
  return [x, y]

