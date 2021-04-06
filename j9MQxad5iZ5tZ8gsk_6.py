
def find_vertex(x):
  a, b = [int(v.replace(' ','')) for v in x.split('x')[:-1]]
  return -b // (2 * a)

