
def add_letters(a):
  
  if (a == []):
    return "z"
  
  CODE = "0abcdefghijklmnopqrstuvwxyz"
  
  Score = 0
  
  Counter = 0 
  Length = len(a)
  
  while (Counter < Length):
    Item = a[Counter]
    Letter = Item.lower()
    Value = CODE.index(Letter)
    Score += Value
    Counter += 1
  
  while (Score > 26):
    Score -= 26
  
  Answer = CODE[Score]
  
  return Answer

