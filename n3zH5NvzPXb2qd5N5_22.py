
def how_mega_is_it(n):
  
  Number = abs(n)
  
  if (Number < 100):
    return "not a mega milestone"
  
  Failsafe = 0
  Value = 10
  Power = 0
  
  while (Failsafe == 0):
  
    Score = Value ** Power
    
    if (Score > Number):
      Failsafe += 1
    else:
      Power += 1
  
  Power -= 2
  
  Prefix = "MEGA " * Power
  Suffix = "milestone"
  
  Answer = Prefix + Suffix
  
  return Answer

