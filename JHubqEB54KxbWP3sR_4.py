
def dist(line, x, y):
  a = line[2:line.index("x")]
  b = line[line.index("x")+1:]
  a = eval(a)
  b = eval(b)
  div = (1 + (a**2))**0.5
  r = (a * x) + (-1 * y) + b
  return round(abs(r)/div, 2)

