
def coloured_triangle(row):
  
  Length = len(row)
  
  Current_Row = row
  Row_Below = ""
  
  while (Length > 1):
  
    First = 0
    Second = 1
    Length = len(Current_Row)
    
    while (Second < Length):
      
      Item_A = Current_Row[First]
      Item_B = Current_Row[Second]
      
      Batch = []
      Batch.append(Item_A)
      Batch.append(Item_B)
      Batch = sorted(Batch)
      
      if (Batch == ["B", "B"]):
        Row_Below = Row_Below + "B"
        First += 1
        Second += 1
      
      elif (Batch == ["B", "G"]):
        Row_Below = Row_Below + "R"
        First += 1
        Second += 1
      
      elif (Batch == ["B", "R"]):
        Row_Below = Row_Below + "G"
        First += 1
        Second += 1
      
      elif (Batch == ["G", "G"]):
        Row_Below = Row_Below + "G"
        First += 1
        Second += 1
      
      elif (Batch == ["G", "R"]):
        Row_Below = Row_Below + "B"
        First += 1
        Second += 1
      
      elif (Batch == ["R", "R"]):
        Row_Below = Row_Below + "R"
        First += 1
        Second += 1
      
      else:
        First += 1
        Second += 1
        
    Current_Row = Row_Below
    Row_Below = ""
    Length = len(Current_Row)
    
  return Current_Row

