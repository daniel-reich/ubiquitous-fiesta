
def add_str_nums(num1, num2):
​
  # Bucket for Grand Total
  Total = 0
  
  # Converting num1 to List
  List_A = list(num1)
  
  # Adding Up Value of List_A (aka num1)
  Multiple = 1
  
  Cursor = -1
  Length = len(List_A)
  End = Length * -1
  
  while (Cursor >= End):
    Item = List_A[Cursor]
    
    if (Item.isdigit()):
      Digit = int(Item)
      Value = Digit * Multiple
      Total += Value
      Multiple *= 10
      Cursor -= 1
    else:
      return "-1"
  
  # Converting num2 to List
  List_B = list(num2)
  
  # Adding Up Value of List_B (aka num2)
  Multiple = 1
  
  Cursor = -1
  Length = len(List_B)
  End = Length * -1
  
  while (Cursor >= End):
    Item = List_B[Cursor]
    
    if (Item.isdigit()):
      Digit = int(Item)
      Value = Digit * Multiple
      Total += Value
      Multiple *= 10
      Cursor -= 1
    else:
      return "-1"
  
  # Giving Answer (if all were digits)
  return str(Total)

