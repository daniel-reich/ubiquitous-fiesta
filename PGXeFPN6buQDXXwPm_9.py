
def trace(lst):
​
  rsum = 0
  for x in range(len(lst)):
    rsum += lst[x][x] 
  
  return rsum

