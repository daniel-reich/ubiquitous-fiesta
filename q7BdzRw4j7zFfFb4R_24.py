
def merge_arrays(a, b):
​
  List_A = a
  List_B = b
  
  Length_A = len(List_A)
  Length_B = len(List_B)
  Shortest = min(Length_A,Length_B)
  
  Answer = []
  
  Cursor = 0
  End = len(List_A)
  
  while (Cursor < Shortest):
    
    Item_A = List_A[Cursor]
    Item_B = List_B[Cursor]
    
    Answer.append(Item_A)
    Answer.append(Item_B)
    
    Cursor += 1
​
  Test_A = Length_A + Length_B
  Test_B = len(Answer)
  Longest = max(Length_A,Length_B)
  
  if (Test_A == Test_B):
    return Answer
  
  else:
    
    while (Cursor < Longest):
​
      if (Length_A == Longest):
        Item = List_A[Cursor]
        Answer.append(Item)
        Cursor += 1
​
      elif (Length_B == Longest):
        Item = List_B[Cursor]
        Answer.append(Item)
        Cursor += 1
​
      else:
        Cursor += 1
​
  return Answer

