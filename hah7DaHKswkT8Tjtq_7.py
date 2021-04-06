
def separate_numbers(s):
  
  Original_Text = str(s)
  End = 1
  Length = len(Original_Text)
  
  while (End < Length):
    
    First = Original_Text[0:End]
    Batch = First
    Next = int(First) + 1
    Span = len(Batch)
    
    while (Span < Length):
      Batch = Batch + str(Next)
      Next += 1
      Span = len(Batch)
      Length = len(Original_Text)
      
    if (Batch == Original_Text):
      return "YES {}".format(First)
    else:
      End += 1
    
  return "NO"

