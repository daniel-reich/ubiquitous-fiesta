
def caesar_cipher(text, key):
  CODE = "abcdefghijklmnopqrstuvwxyz"
  CODE = CODE * key
  
  Coded = ""
  
  Counter = 0
  Length = len(text)
  
  while (Counter < Length):
    Item = text[Counter]
    
    if (Item not in CODE):
      Coded = Coded + Item
      Counter += 1
    else:
      Old = CODE.index(Item)
      New = Old + key
      Letter = CODE[New]
      Coded = Coded + Letter
      Counter += 1
  
  return Coded

