
def how_many_walls(n, w, h):
  a=w*h
  if n>=a:
    return n//a
  elif n<a:
    return 0

