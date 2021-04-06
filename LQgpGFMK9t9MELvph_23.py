
def get_diagonals(lst):
  
  if (lst == []):
    return [[],[]]
  
  Length = len(lst)
  
  if (Length == 1):
    Answer = []
    Answer.append(lst[0])
    Answer.append(lst[0])
    return Answer
  
  if (Length == 2):
    return lst
  
  # Assuming Length is Greater Than Two
  # Bucket for Final Answer
  
  Answer = []
  
  # Going Top Left to Bottom Right
  
  Batch = []
  
  Counter = 0
  Length = len(lst)
  
  while (Counter < Length): 
    Item = lst[Counter][Counter]
    Batch.append(Item)
    Counter += 1
  
  Answer.append(Batch)
  
  # Going Top Right to Bottom Left
  
  Batch = []
  
  Counter = 0
  Cursor = -1
  Length = len(lst)
  End = Length * -1
  
  while (Counter < Length):
    Item = lst[Counter][Cursor]
    Batch.append(Item)
    Counter += 1
    Cursor -= 1
  
  Answer.append(Batch)
  
  # Giving Answer
  return Answer

