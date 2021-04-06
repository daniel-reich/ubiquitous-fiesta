
def is_ascending(s):
  
  Sample_A = str(s)
  Length = len(Sample_A)
  Ending = 1
  
  while (Ending < Length - 1):
    
    Sample_B = Sample_A[0:Ending]
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
      Ending += 1
    
  return False

