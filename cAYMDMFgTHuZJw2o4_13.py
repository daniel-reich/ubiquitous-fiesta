
def reverse_image(image):
  
  Sample = image
  
  Negative = []
  
  Counter = 0
  Length = len(image)
  
  while (Counter < Length):
  
    Batch = []
    Item = Sample[Counter]
    
    Cursor = 0
    Span = len(Item)
    
    while (Cursor < Span):
      
      Thing = Sample[Counter][Cursor]
      
      if (Thing == 0):
        Batch.append(1)
        Cursor += 1
      elif (Thing == 1):
        Batch.append(0)
        Cursor += 1
      else:
        Cursor += 1
      
    Negative.append(Batch)
    Counter += 1
  
  return Negative

