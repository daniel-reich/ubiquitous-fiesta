
def weight_allowed(car, p, max_weight):
  
  Total_A = 0
  
  for x in p:
    Total_A += x
    
  Total_A += car
  
  Total_A *= 0.453592
  Total_B = max_weight
  
  if (Total_A <= Total_B):
    return True
  else:
    return False

