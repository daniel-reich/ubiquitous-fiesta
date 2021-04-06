
def legendre(p, n):
  
  Total = 0
  Counter = 1
  
  Top = n
  Bottom = p ** Counter
  
  while (Bottom <= Top):
    
    Top = n
    Bottom = p ** Counter
    
    Value = int(Top/Bottom)
    Total += Value
    Counter += 1
  
  return Total

