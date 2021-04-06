
def repeated(s):
  
  if (len(s) == 1):
    return False
  
  Divider = 2
  Ceiling = len(s)
  
  while (Divider < Ceiling):
    
    Sample_A = s
    Sample_B = s[0:Divider]
    
    Batch = s[0:Divider]
    
    Length_A = len(Sample_A)
    Length_B = len(Sample_B)
    
    while (Length_B < Length_A):
      Sample_B = Sample_B + Batch
      Length_A = len(Sample_A)
      Length_B = len(Sample_B)
    
    if (Sample_A == Sample_B):
      return True
    else:
      Divider += 1
  
  return False

