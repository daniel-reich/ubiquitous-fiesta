
def find_longest(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
  
  if (len(Parameters) == 1):
    Parameters.append("X")
  
  Sample = Parameters[0]
  Answer = Parameters[1]
  
  if (type(Sample) == str):
    
    Code_01 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Code_02 = "abcdefghijklnnopqrstuvwxyz"
    
    Revised = ""
    
    Counter = 0
    Length = len(Sample)
    
    while (Counter < Length):
      
      Item = Sample[Counter]
      
      if (Item.isalpha()):
        Revised = Revised + Item.lower()
        Counter += 1
      else:
        Revised = Revised + " "
        Counter += 1
    
    while ("  " in Revised):
      Revised = Revised.replace("  ", " ")
    
    while (Revised[0] == " "):
      Revised = Revised[1:]
    
    while (Revised[-1] == " "):
      Revised = Revised[0:-1]
    
    Blocks = Revised.split(" ")
    return find_longest(Blocks, Answer)
    
  elif (Sample == []):
    return Answer
  
  elif (len(Sample[0]) > len(Answer)):
    Answer = Sample[0]
    Sample = Sample[1:]
    return find_longest(Sample, Answer)
  
  else:
    Sample = Sample[1:]
    return find_longest(Sample, Answer)

