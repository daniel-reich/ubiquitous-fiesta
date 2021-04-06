
def three_letter_collection(s):
  
  Pieces = []
  Start = 0
  End = 3
  
  Counter = 0
  Length = len(s)
  
  while (End <= Length):
    Block = s[Start:End]
    Pieces.append(Block)
    Start += 1
    End += 1
  
  return sorted(Pieces)

