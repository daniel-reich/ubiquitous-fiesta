
def is_disarium(n):
  n = str(n)
  total = 0
  for i,x in enumerate(n):
    total +=int(x)**(i+1)
  return total==int(n)

