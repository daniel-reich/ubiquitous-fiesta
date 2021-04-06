
def correct_sentences(s):
  
  Sample = s
  
  while ("  " in Sample):
    Sample = Sample.replace("  ", " ")
  
  while (Sample[0] == " "):
    Sample = Sample[1:]
  
  while (Sample[-1] == " "):
    Sample = Sample[0:-1]
  
  Answer = Sample[0].upper()
  
  Counter = 1
  Length = len(Sample)
  
  while (Counter < Length):
    
    Item = Sample[Counter]
    
    if (Item.isupper()):
      Answer = Answer + ". " + Item
      Counter += 1
    else:
      Answer = Answer + Item
      Counter += 1
      
  Answer = Answer + "."
  Answer = Answer.replace(" .", ".")
  return Answer

