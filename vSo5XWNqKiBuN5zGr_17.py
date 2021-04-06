
def divide(x, y):
  # Your recursive solution here.
  if abs(x)<abs(y):
    return 0
  else: 
    return (-1)**(x*y<0)+divide(x-(-1)**(x*y<0)*y, y)

