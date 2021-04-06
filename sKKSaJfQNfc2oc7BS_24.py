
def sle(m):
  m = list(map(tuple,m))
  a,b,c = m[0]
  d,e,f =m[1]
  try:
    y = (f*a-d*c)//((-d)*b+e*a)
    x = (c-b*y)//a
  except:
    return False
  return x,y

