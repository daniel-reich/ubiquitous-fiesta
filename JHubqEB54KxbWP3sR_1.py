
def dist(line, x, y):
  m, b = [eval(v) for v in line.split('=')[1].split('x')]
  return round(abs(-x*m + y-b)/((1+m**2)**.5),2)

