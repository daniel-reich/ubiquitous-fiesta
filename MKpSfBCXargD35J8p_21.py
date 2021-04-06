
def journey_distance(n):
  
  Travelled = 0
  
  Spent = 0
  Budget = n
  
  while (Spent < Budget):
    
    if (Travelled == 0):
      Spent += 3
      Travelled += 1
    else:
      Spent += 2
      Travelled += 1
      
  return Travelled

