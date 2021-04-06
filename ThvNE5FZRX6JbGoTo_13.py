
def inverter(Passage, Method):
  
  Blocks = Passage.split(" ")
  
  if (Method == "P"):
    
    Sentence = ""
    
    Cursor = -1
    Length = len(Blocks)
    End = Length * -1
    
    while (Cursor >= End):    
      Word = Blocks[Cursor]
      Sentence = Sentence + Word + " "
      Cursor -= 1
  
    Sentence = Sentence.rstrip(" ")
    Sentence = Sentence.capitalize()
    
    return Sentence
  
  elif (Method == "W"):
  
    Sentence = ""
    
    Counter = 0
    Length = len(Blocks)
    
    while (Counter < Length):
      Word = str(Blocks[Counter])
      Tweaked = Word[::-1]
      Sentence = Sentence + Tweaked + " "
      Counter += 1
    
    Sentence = Sentence.rstrip(" ")
    Sentence = Sentence.capitalize()
    
    return Sentence
  
  else:
    return "Something else"

