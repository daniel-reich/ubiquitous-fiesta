
def fire(matrix, coordinates):
  
  CODE = "ABCDE"
  Target = str(coordinates)
  
  First = str(Target[0])
  Second = str(Target[1])
  
  Row = CODE.index(First)
  Column = int(Second) - 1
  
  Outcome = matrix[Row][Column]
  
  if (Outcome == "."):
    return "splash"
  elif (Outcome == "*"):
    return "BOOM"
  else:
    return "I don't know!"

