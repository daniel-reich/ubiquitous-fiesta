
def is_narcissistic(n):
​
  Text = str(n)
  Power = len(Text)
  
  Total = 0
  
  Counter = 0
  Length = len(Text)
  
  while (Counter < Length):
    Item = Text[Counter]
    Digit = int(Item)
    Score = Digit ** Power
    Total += Score
    Counter += 1
  
  if (Total == n):
    return True
  else:
    return False

