
from functools import reduce
​
def soroban(frame):
  upper = int(frame[1].replace("|","0").replace("O","5"))
  
  lower = ""
  for column in range(7):
    s = "".join([frame[row][column] for row in range(3,8)])
    n = len(s.split("|")[0])
    lower += str(n)
    
  lower = int(lower)
  
  return upper+lower

