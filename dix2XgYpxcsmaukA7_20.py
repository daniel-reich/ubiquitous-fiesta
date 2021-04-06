
############################################################
#     Sub Function 
############################################################
​
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
############################################################
#     MAIN FUNCTION
############################################################
​
def express_factors(n):
  
  Prime_Factors = []
  
  Divisor = 2
  Remaining = n
  
  while (Remaining > 1):
    
    Test_A = FNC_Prime_Number_Checker(Divisor)
    Test_B = Remaining % Divisor
    
    if (Test_A == True) and (Test_B == 0):
      Prime_Factors.append(Divisor)
      Remaining /= Divisor
    else:
      Divisor += 1
  
  Checked = []
  Equation = []
  
  Counter = 0
  Length = len(Prime_Factors)
  
  while (Counter < Length):
    
    Number = Prime_Factors[Counter]
    Power = Prime_Factors.count(Number)
    
    if (Number not in Checked) and (Power > 1):
      Passage = str(Number) + "^" + str(Power)
      Equation.append(Passage)
      Checked.append(Number)
      Counter += 1
    elif (Number not in Checked) and (Power == 1):
      Passage = str(Number)
      Equation.append(Passage)
      Checked.append(Number)
      Counter += 1
    else:
      Counter += 1
      
  Link = " x "
  Answer = Link.join(Equation)
  return Answer

