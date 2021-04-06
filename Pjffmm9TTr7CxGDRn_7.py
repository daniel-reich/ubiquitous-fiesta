
def is_ascending(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) == 1):
    Parameters.append(1)
    
  Text = Parameters[0]
  Divider = Parameters[1]
  Ceiling = len(Text) - 1
  
  if (Divider == Ceiling):
    return False
  
  else:
    
    Sample_A = Text
    Sample_B = Text[0:Divider]
    
    Number = int(Sample_B) + 1
    
    Length_A = len(Sample_A)
    Length_B = len(Sample_B)
    
    while (Length_B < Length_A):
      Sample_B = Sample_B + str(Number)
      Number += 1
      Length_A = len(Sample_A)
      Length_B = len(Sample_B)
    
    if (Sample_A == Sample_B):
      return True
    else:
      Divider += 1
      return is_ascending(Text, Divider)

