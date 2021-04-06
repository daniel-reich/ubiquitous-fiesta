
def lemonade(bills):
  
  # Variables to Denote 'Till'
  Fives = 0
  Tens = 0
  Twenties = 0
  
  Counter = 0
  Length = len(bills)
  
  while (Counter < Length):
    
    # Filling 'Till' with Note of Payment
    Paying_With = bills[Counter]
    
    if (Paying_With == 5):
      Fives += 1
    elif (Paying_With == 10):
      Tens += 1
    elif (Paying_With == 20):
      Twenties += 1
    else:
      return "ERROR"
    
    # Establishing Change Required
    Change = Paying_With - 5
    
    # Dispensing Change (in theory)
    
    if (Change == 0):
      Counter += 1
    
    else:
      
      while (Change >= 20) and (Twenties > 0):
        Twenties -= 1
        Change -= 20
      
      while (Change >= 10) and (Tens > 0):
        Tens -= 1
        Change -= 10
      
      while (Change > 0):
        Fives -= 1
        Change -= 5
    
      # Testing the 'in theory' part of the above comment
      if (Twenties < 0) or (Tens < 0) or (Fives < 0):
        return False
      else:
        Counter += 1
  
  # If everyone gets their change
  return True

