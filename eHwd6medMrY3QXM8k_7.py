
############################################################
#   Sub Function 1
############################################################
​
def FNC_Batch_Builder(Sample, Size):
​
  Blocks = []
  
  Counter = 0
  Length = len(Sample)
  
  while (Counter < Length):
    
    Batch = ""
    Added = 0
    Required = Size
  
    while (Added < Required) and (Counter < Length):
      Item = Sample[Counter]
      Batch = Batch + Item
      Added += 1
      Counter += 1
    
    Number = int(Batch)
    Blocks.append(Number)
    Batch = ""
  
  if (Batch != ""):
    Number = int(Batch)
    Blocks.append(Number)
        
  return Blocks
​
############################################################
#   Sub Function 2
############################################################
​
def FNC_Consecutive_Up_Checker(Sample):
​
  First = 0
  Second = 1
  Length = len(Sample)
  
  while (Second < Length):
    
    Number_A = Sample[First]
    Number_B = Sample[Second]
    Difference = Number_B - Number_A
    
    if (Difference == 1):
      First += 1
      Second += 1
    else: 
      return False
  
  return True
​
############################################################
#   Sub Function 3
############################################################
​
def FNC_Consecutive_Down_Checker(Sample):
​
  First = 0
  Second = 1
  Length = len(Sample)
  
  while (Second < Length):
    
    Number_A = Sample[First]
    Number_B = Sample[Second]
    Difference = Number_A - Number_B
    
    if (Difference == 1):
      First += 1
      Second += 1
    else: 
      return False
  
  return True
​
############################################################
#   MAIN FUNCTION
############################################################
​
def is_consecutive(Sample):
​
  Testing = 1
  Ceiling = len(Sample)
  
  while (Testing < Ceiling):
    
    Blocks = FNC_Batch_Builder(Sample, Testing)
    
    if FNC_Consecutive_Up_Checker(Blocks):
      return True
    elif FNC_Consecutive_Down_Checker(Blocks):
      return True
    else:
      Testing += 1
      
  return False

