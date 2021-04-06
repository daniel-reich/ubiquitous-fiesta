
def is_consecutive(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
  
  if (len(Parameters) == 1):
    Parameters.append(1)
​
  Text = Parameters[0]
  Divider = Parameters[1]
  Length = len(Text)
  
  if (Divider == Length):
    return False
  else:
    
    Sample_A1 = Text
    Sample_A2 = Text[0:Divider]
    Number_A2 = int(Sample_A2) + 1
    
    Length_A1 = len(Sample_A1)
    Length_A2 = len(Sample_A2)
    
    while (Length_A2 < Length_A1):
      Sample_A2 = Sample_A2 + str(Number_A2)
      Number_A2 += 1
      Length_A1 = len(Sample_A1)
      Length_A2 = len(Sample_A2)
    
    Sample_B1 = Text
    Sample_B2 = Text[0:Divider]
    Number_B2 = int(Sample_B2) - 1
    
    Length_B1 = len(Sample_B1)
    Length_B2 = len(Sample_B2)
    
    while (Length_B2 < Length_B1):
      Sample_B2 = Sample_B2 + str(Number_B2)
      Number_B2 -= 1
      Length_B1 = len(Sample_B1)
      Length_B2 = len(Sample_B2)
    
    if (Sample_A1 == Sample_A2) or (Sample_B1 == Sample_B2):
      return True
    else:
      Divider += 1
      return is_consecutive(Text, Divider)

