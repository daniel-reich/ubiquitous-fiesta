
import numpy as np
​
def generate_rug(n, direction):
  rug = []
  pivot = 0
  for i in range(n):
    row = np.zeros(n)
    
    for j in range(0, pivot):
      row[pivot - j - 1] = j + 1
    
    for j in range(pivot, n):
      row[j] = j - pivot
      
    pivot += 1
    
    row = list(row)
    if direction == "right":
      row.reverse()
      
    rug.append(row)
    
  return rug

