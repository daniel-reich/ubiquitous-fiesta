
def simple_check(a, b):
​
  if (a > b):
    Highest = a
    Lowest = b
  else:
    Highest = b
    Lowest = a
    
  Answer = 0
  
  while (Lowest > 0):
    
    if (Highest % Lowest == 0):
      Answer += 1
      Highest -= 1
      Lowest -= 1
    else:
      Highest -= 1
      Lowest -= 1
    
  return Answer

