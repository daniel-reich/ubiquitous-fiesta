
def find_vertex(x):
  y = x.replace("x", "").replace(" ", "").replace("+", " +").replace("-", " -")
  y = y.split()
  y.pop(2)
​
  a = int(y[0])
  b = int(y[1])
  c = 2 * a
​
  return -b // c

