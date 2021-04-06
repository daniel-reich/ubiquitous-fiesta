
import math
​
def spin_around(lst):
  
  Moves = 0
  
  for x in lst:
    if (x == "left"):
      Moves += 1
    if (x == "right"):
      Moves -= 1
      
  Answer = math.floor(abs(Moves/4))
  return Answer

