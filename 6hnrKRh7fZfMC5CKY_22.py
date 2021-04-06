
def look_and_say(n):
  
  Sample = str(n)
  Length = len(Sample)
  
  if (Length % 2 != 0):
    return "invalid"
  
  Revised = ""
  
  First = 0
  Second = 1
  Length = len(Sample)
  
  while (Second < Length):
    Repeat = int(Sample[First])
    Character = str(Sample[Second])
    Batch = Repeat * Character
    Revised = Revised + Batch
    First += 2
    Second += 2
  
  Answer = int(Revised)
  
  return Answer

