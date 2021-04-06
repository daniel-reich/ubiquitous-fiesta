
def dist(line, x, y):
  a, b=[eval(t) for t in line[2:].split('x')]
  return round(abs(a*x-y+b)/(a**2+1)**0.5,2)

