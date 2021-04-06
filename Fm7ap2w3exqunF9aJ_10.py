
def count_lone_ones(n):
  
  Text = str(n)
  
  if (n == 1):
    return 1
  
  elif (n >= 10) and (n <= 19) and (n != 11):
    return 1
  
  elif (Text[-1] == "1") and (n > 20) and (n < 100):
    return 1
  
  else:
    Lonely = 0
    Start = 0
    End = 3
    Length = len(Text)
    
    while (End < Length):
      
      Block = Text[Start:End]
      
      if (Block[0] != "1") and (Block[1] == "1") and (Block[2] != "1"):
        Lonely += 1
        Start += 1
        End += 1
      else:
        Start += 1
        End += 1
  
  if (Text[0] == "1") and (Text[1] != "1"):
    Lonely += 1
  
  if (Text[-1] == "1") and (Text[-2] != "1"):
    Lonely += 1
  
  return Lonely

