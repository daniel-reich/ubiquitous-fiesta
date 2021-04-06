
def find_vertex(x):
  a, b, c = [int(i.replace('x', '')) for i in x.split() if i not in ['+', '-']]
  
  return -b // (2 * a)

