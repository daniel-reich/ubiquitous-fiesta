
import sys
def stock_picker(lst):
  
  profit = 0;
  min = sys.maxsize
  for i in lst:
    if (i < min):
      min = i
      
    if (i - min > profit):
      profit = i - min
  
      
  if (profit == 0):
    return -1
    
  else:
    return profit

