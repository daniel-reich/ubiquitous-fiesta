
def list_operation(x, y, n):
  p= []
  lolo = range(x, y+1)
  for num in lolo:
    if num%n == 0:
      p.append(num)
  return(p)

