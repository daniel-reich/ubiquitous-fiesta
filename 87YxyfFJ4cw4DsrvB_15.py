
import random
import math
​
def generate_rug(n):
​
  if n == 1:
    return [[0]]
  height = int(math.floor(n/2))
  toReturn = []
  for row in range(0,n):
    if row >= int(math.ceil(n/2)):
      toReturn.append(toReturn[n-1-row])
    else:
      toReturn.append([])
      for column in range(0,n):
        if column >= (math.ceil(n/2)):
          toReturn[row].append(toReturn[row][n-1-column])
        else:
          for _ in range(0, n-1):
            if row == _ or column == _:
              toReturn[row].append(height-_)
              break
      
  return toReturn

