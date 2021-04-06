
def prime_in_range(n1, n2):
  
  Range = []
  
  Start = n1
  End = n2
  
  while (Start <= End):
    Range.append(Start)
    Start += 1
  
  Counter = 0
  Length = len(Range)
  
  while (Counter < Length):
    
    Value = Range[Counter]
    Factor = 1
    Factors = []
    
    while (Factor <= Value):
      
      if (Value % Factor == 0):
        Factors.append(Factor)
        Factor += 1
      else:
        Factor += 1
    
    Span = len(Factors)
    
    if (Span == 2):
      return True
    else:
      Counter += 1
        
  return False

