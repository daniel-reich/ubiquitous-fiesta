
def is_magic(Square):
  
  #   Covering Empty Square Possibility
  if (Square == []):
    return True
  
  #   Establishing Target Total
  Target = 0
  
  Counter = 0
  Length = len(Square[0])
  
  while (Counter < Length):
    Value = Square[0][Counter]
    Target += Value
    Counter += 1
  
  #   Establishing Highest Valid Number
  Highest = len(Square) ** 2
  
  #   Checking Columns
  CC = 0
  CL = len(Square[0])
  
  RC = 0
  RL = len(Square)
  
  while (CC < CL) and (RC < RL):
    
    Total = 0
    
    while (CC < CL):
      
      Value = Square[RC][CC]
      
      if (Value < 0) or (Value % 1 != 0) or (Value > Highest):
        return False
      else:
        Total += Value
        CC += 1
      
    if (Total != Target):
      return False
    else:
      CC = 0
      RC += 1
  
  #   Checking Rows
  CC = 0
  CL = len(Square[0])
  
  RC = 0
  RL = len(Square)
  
  while (CC < CL) and (RC < RL):
    
    Total = 0
    
    while (RC < RL):
      
      Value = Square[RC][CC]
      
      if (Value < 0) or (Value % 1 != 0) or (Value > Highest):
        return False
      else:
        Total += Value
        RC += 1
      
    if (Total != Target):
      return False
    else:
      CC += 1
      RC = 0
      
  #   Checking Diagonals
  Total_A = 0
  Total_B = 0
  
  Counter = 0
  Cursor = -1
  Length = len(Square)
  
  while (Counter < Length):
    
    Value_A = Square[Counter][Counter]
    Total_A += Value_A
    
    Value_B = Square[Counter][Cursor]
    Total_B += Value_B
  
    Counter += 1
    Cursor -= 1
  
  #   Making Final Tests
  if (Total_A != Target):
    return False
  elif (Total_B != Target):
    return False
  else:
    return True

