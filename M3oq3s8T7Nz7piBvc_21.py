
def even_odd_string(txt):
​
  Even = ""
  Odd = ""
  
  Counter = 0
  Length = len(txt)
  
  while (Counter < Length):
    
    Letter = txt[Counter]
    
    if (Counter % 2 == 0):
      Even = Even + Letter
      Counter += 1
    else:
      Odd = Odd + Letter
      Counter += 1
      
  Answer = Even + " " + Odd
  return Answer

