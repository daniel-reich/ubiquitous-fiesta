
############################################################
#     Sub Function
############################################################
​
def FNC_Simple_Number_Checker(Target):
​
  Power = 1
  Text = str(Target)
  Total = 0
  
  Counter = 0
  Length = len(Text)
  
  while (Counter < Length):
    Item = Text[Counter]
    Digit = int(Item)
    Score = Digit ** Power
    Total += Score
    Power += 1
    Counter += 1
  
  if (Total == Target):
    return True
  else:
    return False
  
​
############################################################
#     MAIN FUNCTION
############################################################
​
def simple_numbers(a, b):
​
  if (a <= b):
    Value = a
    Ceiling = b
  else:
    Value = b
    Ceiling = a
    
  Answer = []
  
  while (Value <= Ceiling):
    
    if FNC_Simple_Number_Checker(Value):
      Answer.append(Value)
      Value += 1
    else:
      Value += 1
  
  return Answer

