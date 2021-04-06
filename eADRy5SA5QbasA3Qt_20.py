
def is_harshad(n):
​
  Total = 0
  Text = str(n)
  
  Counter = 0
  Length = len(Text)
  
  while (Counter < Length):
    Item = Text[Counter]
    Value = int(Item)
    Total += Value
    Counter += 1
  
  if (n % Total == 0):
    return True
  else:
    return False

