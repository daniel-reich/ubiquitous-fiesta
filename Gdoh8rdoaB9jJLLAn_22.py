
def summation(exp, i):
  
  Total = 0
  
  Cursor = 1
  End = i
  
  while (Cursor <= End):
    
    Equation = str(exp)
    New = str(Cursor)
    Equation = Equation.replace("n", New)
    Value = eval(Equation)
    Total += Value
    Cursor += 1
  
  Answer = round(Total,1)
  
  return Answer

