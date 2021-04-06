
def FNC_Prime_Number_Checker(Number):
​
  Divisor = 2
  
  while (Divisor < Number):
    
    if (Number % Divisor == 0):
      return False
    else:
      Divisor += 1
      
  return True
​
def goldbach_conjecture(n):
​
  if (n < 2) or (n % 2 != 0) or (n % 1 != 0):
    return []
    
  else:
    Value = 2
    Ceiling = n
    
    while (Value < Ceiling):
      Difference = n - Value
      Test_A = FNC_Prime_Number_Checker(Value)
      Test_B = FNC_Prime_Number_Checker(Difference)
      
      if (Test_A and Test_B):
        Answer = []
        Answer.append(Value)
        Answer.append(Difference)
        return Answer
      else:
        Value += 1
        
    return []

