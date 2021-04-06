
def get_missing_letters(s):
​
  Sample = str(s)
  Sample = Sample.lower()
  Sample = list(Sample)
  Sample = sorted(Sample)
  
  Code = "abcdefghijklmnopqrstuvwxyz" 
  Complete = list(Code)
  Complete = sorted(Complete)
  
  Wanted = []
  
  CC = 0
  CL = len(Code)
    
  SC = 0
  SL = len(Sample)
  
  while (CC < CL) and (SC < SL):    
    Code_Item = str(Code[CC])
    Sample_Item = str(Sample[SC])
    
    if (Sample_Item != Code_Item):
      Wanted.append(Code_Item)
      CC += 1
    else:
      CC += 1
      SC += 1
    
  while (CC < CL):
    Code_Item = str(Code[CC])
    Wanted.append(Code_Item)
    CC += 1
    
  Missing = ""
  
  Counter = 0
  Length = len(Wanted)
  
  while (Counter < Length):
    Item = str(Wanted[Counter])
    Missing = Missing + Item
    Counter += 1
  
  return Missing

