
def FNC_Digit_Totaller(Number):
​
  Text = str(Number)
  Total = 0
  
  Counter = 0
  Length = len(Text)
  
  while (Counter < Length):
    Item = Text[Counter]
    Digit = int(Item)
    Total += Digit
    Counter += 1
    
  return Total
​
def mubashir_function(a, b):
  
  Value_A = FNC_Digit_Totaller(a)
  Value_B = FNC_Digit_Totaller(b)
  
  Answer = Value_A * Value_B
  return Answer

