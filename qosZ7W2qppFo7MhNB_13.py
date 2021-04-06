
import math
​
def hex_distance(grid):
  A, B = find_start_end(grid)
  Ax, Ay = A
  Bx, By = B
  
  steps = 0
  while Ax != Bx or Ay != By:
    if Ay < By:
      Ay += 1
      Ax += math.copysign(1, Bx - Ax)
    elif Ay > By:
      Ay -= 1
      Ax += math.copysign(1, Bx - Ax)
    else:
      Ax += math.copysign(1, Bx - Ax) * 2
      
    steps += 1
    
  return steps
  
def find_start_end(grid):
  return [ (x, y) for y, string in enumerate(grid)
                  for x, char in enumerate(string)
                  if char == 'x' ]

