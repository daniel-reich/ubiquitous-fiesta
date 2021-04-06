
def right_triangle(x, y, z):
  
  if (x <= 0) or (y <= 0) or (z <= 0):
    return False
  
  Numbers = []
  Numbers.append(x)
  Numbers.append(y)
  Numbers.append(z)
  
  Numbers = sorted(Numbers)
  
  Value_A = Numbers[0] * Numbers[0]
  Value_B = Numbers[1] * Numbers[1]
  Value_C = Numbers[2] * Numbers[2]
  
  if (Value_A + Value_B == Value_C):
    return True
  else:
    return False

