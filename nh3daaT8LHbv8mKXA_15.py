
def text_to_num(phone):
  
  Sample = str(phone)
  
  Revised = ""
  
  Counter = 0
  Length = len(Sample)
  
  while (Counter < Length):
​
    Piece = Sample[Counter]
​
    if (Piece in "ABC"):
      Revised = Revised + "2"
      Counter += 1
    elif (Piece in "DEF"):
      Revised = Revised + "3"
      Counter += 1
    elif (Piece in "GHI"):
      Revised = Revised + "4"
      Counter += 1
    elif (Piece in "JKL"):
      Revised = Revised + "5"
      Counter += 1
    elif (Piece in "MNO"):
      Revised = Revised + "6"
      Counter += 1
    elif (Piece in "PQRS"):
      Revised = Revised + "7"
      Counter += 1
    elif (Piece in "TUV"):
      Revised = Revised + "8"
      Counter += 1
    elif (Piece in "WXYZ"):
      Revised = Revised + "9"
      Counter += 1
    else:
      Revised = Revised + Piece
      Counter += 1        
​
  return Revised

