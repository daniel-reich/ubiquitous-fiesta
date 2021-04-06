
def safecracker(start, increments):
  n1 = move(start, increments[0], True)
  n2 = move(n1, increments[1], False)
  n3 = move(n2, increments[2], True)
  
  return [n1, n2, n3]
  
​
def move(number, increment, clockwise):
  a = (number - increment) if clockwise else (number + increment)
  
  if clockwise:
    return a if (a > 0) else (100 + a)
  else:
    return a if (a < 100) else (a - 100)

