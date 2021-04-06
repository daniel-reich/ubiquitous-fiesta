
def find_vertex(a, b, c):
  x = -b / (2*a)
  y = a * x**2 + b * x + c
  rounded_x = round(x*100)/100
  rounded_y = round(y*100)/100
  return [rounded_x, rounded_y]

