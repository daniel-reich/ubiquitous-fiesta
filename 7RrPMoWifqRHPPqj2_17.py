
def safecracker(start, increments):
  a,b,c = increments
  x = (start-a)%100
  y = (x+b)%100
  z = (y-c)%(100)
  return [x,y,z]

