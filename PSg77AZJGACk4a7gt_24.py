
def meme_sum(a, b):
  
  # Converting Parameters to String
  
  Text_A = str(a)
  Length_A = len(Text_A)
  
  Text_B = str(b)
  Length_B = len(Text_B)
  
  # Making Sure Both Strings Are Same Length
  
  while (Length_A < Length_B):
    Text_A = "0" + Text_A
    Length_A = len(Text_A)
    Length_B = len(Text_B)
    
  while (Length_B < Length_A):
    Text_B = "0" + Text_B
    Length_A = len(Text_A)
    Length_B = len(Text_B)
    
  # Bucket for Answer
  Answer = ""
  
  # Performing 'Mathematics'
  
  Counter = 0
  Length = len(Text_A)
  
  while (Counter < Length):
    
    Item_A = Text_A[Counter]
    Digit_A = int(Item_A)
    
    Item_B = Text_B[Counter]
    Digit_B = int(Item_B)
    
    Score = Digit_A + Digit_B
    Passage = str(Score)
    
    Answer = Answer + Passage
    Counter += 1
    
  # Converting Answer to Integer and Giving Answer
  Answer = int(Answer)
  return Answer

