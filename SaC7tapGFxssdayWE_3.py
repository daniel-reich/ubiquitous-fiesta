
def find_vertex(a, b, c):
  x = -b/(2*a)
  if x==-0.0:
    x=0
  y = (a*x**2)+(b*x)+c
  return [x,y]

