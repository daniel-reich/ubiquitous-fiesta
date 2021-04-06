
def gimme_the_letters(spectrum):
  
  Sample = str(spectrum)
  Letters = Sample.lower()
  
  Code = " abcdefghijklmnopqrstuvwxyz"
  
  First = Letters[0]
  Last = Letters[2]
  
  Start = Code.index(First)
  End = Code.index(Last)
    
  Counter = Start
  Range = ""
  
  while (Counter <= End):
    Range = Range + Code[Counter]
    Counter += 1
  
  Test = Sample[0]
  
  if (Test.isupper()):
    Range = Range.upper()
  else:
    Range = Range
  
  return Range

