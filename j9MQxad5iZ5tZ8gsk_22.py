
def find_vertex(x):
  a,b,c = map(int, x.replace('x','').replace('+', '').split())
  
  return -b//(2*a)

