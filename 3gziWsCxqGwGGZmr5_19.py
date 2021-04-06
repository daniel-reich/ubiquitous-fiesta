
############################################################
#   Sub Function
############################################################
​
def FNC_Prime_Number_Checker(Number):
​
  Factors = []
  Tester = 1
  
  while (Tester <= Number):
    
    if (Number % Tester == 0):
      Factors.append(Tester)
      Tester += 1
    else:
      Tester += 1
  
  Span = len(Factors)
  
  if (Span == 2):
    return True
  else:
    return False
​
############################################################
#   MAIN FUNCTION
############################################################
​
def fat_prime(a, b):
  
  Answer = max(a,b)
  
  while (Answer >= min(a,b)):
  
    if FNC_Prime_Number_Checker(Answer):
      return Answer
    else:
      Answer -= 1
      
  return "No Prime Number in Range"

