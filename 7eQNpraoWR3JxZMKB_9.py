
def my_sub(x, y): 
  if x < y: x , y = y , x
  while (y != 0): 
    borrow = (~x) & y 
    x = x ^ y 
    y = borrow << 1
  return x

