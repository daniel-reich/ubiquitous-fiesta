
def wrap_around(string, offset):
  
  Sample = str(string)
  
  Length = len(Sample)
  Roll = offset
  
  while (Roll < 0) or (Roll > Length):
  
    if (Roll > Length):
      Roll -= Length
    elif (Roll < 0):
      Roll += Length
    else:
      Roll = Roll
  
  Left = Sample[0:Roll]
  Right = Sample[Roll:]
  
  Answer = Right + Left
  
  return Answer

