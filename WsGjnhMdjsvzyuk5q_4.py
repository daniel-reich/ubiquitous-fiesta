
def dashed(txt):
  
  Revised = ""
  
  Counter = 0
  Length = len(txt)
  
  while (Counter < Length):
    Letter = txt[Counter]
    
    if (Letter in "AEIUOaeiuo"):
      Revised = Revised + "-" + Letter + "-"
      Counter += 1
    else:
      Revised = Revised + Letter
      Counter += 1
  
  return Revised

