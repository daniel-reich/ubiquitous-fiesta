
def dist(line, x, y):
  m = float(eval(line.split('x')[0].split('=')[1]))
  c = float(eval(line.split('x')[1]))
  dist = abs((m*x)-y+c)/((m**2+1)**(1/2))
  return round(dist,2)

