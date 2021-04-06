
def full_key_name(piece):
  
  Blocks = piece.split(" ")
  
  Final_Word = str(Blocks[-1])
  Final_Letter = Final_Word[0]
  
  if (Final_Letter.isalpha()) and (Final_Letter.islower()):
    Ending = "minor"
    
  if (Final_Letter.isalpha()) and (Final_Letter.isupper()):
    Ending = "major"
    
  Final_Word = str(Blocks[-1])
  Final_Word = Final_Word.title()
  Blocks[-1] = Final_Word
  
  Blocks.append(Ending)
  
  Passage = ""
  
  Counter = 0 
  Length = len(Blocks)
  
  while (Counter < Length):
    Item = Blocks[Counter]  
    Passage = Passage + Item + " "
    Counter += 1
  
  Passage = Passage.rstrip(" ")
  
  return Passage

