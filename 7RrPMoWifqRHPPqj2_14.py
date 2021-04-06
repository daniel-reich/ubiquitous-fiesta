
def safecracker(start, increments):
  a,b,c = increments
  a = start-a
  b = a+b
  c = b-c
  return [a%100,b%100,c%100]

