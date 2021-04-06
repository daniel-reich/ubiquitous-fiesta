
def consecutive_sum(n):
  
  Failsafe = 0;
  Start = 1
  Addition = 1
  Total = 0
  
  while (Failsafe == 0):
  
    while (Total < n):
      Total += Addition
      Addition += 1
      
    if (Total == n):
      return True
    else:
      Total = 0
      Start += 1
      Addition = Start
      
    if (Start == n):
      Failsafe += 1
    
  return False

