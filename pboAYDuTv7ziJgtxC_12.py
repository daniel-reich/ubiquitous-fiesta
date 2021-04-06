
def min_turns(current, target):
  
  Sample = str(current)
  Target = str(target)
  
  Turns = 0
  
  Counter = 0
  Length = len(Target)
  
  while (Counter < Length):
    
    Digit_A = int(Sample[Counter])
    Digit_B = int(Target[Counter])
    
    Test_A = abs(Digit_A - Digit_B)
    Test_B = 10 - Test_A
    
    if (Test_A < Test_B):
      Turns += Test_A
    else:
      Turns += Test_B
    
    Counter += 1
    
  return Turns

