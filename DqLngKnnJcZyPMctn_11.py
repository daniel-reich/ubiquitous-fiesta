
def stock_picker(lst):
  
  Maximum_Profit = -1
  
  Counter = 0
  Length = len(lst)
  
  while (Counter < Length):
  
    Cursor = Counter
    Span = len(lst)
  
    while (Cursor < Span):
      
      Selling_Price = lst[Cursor]
      Buying_Price = lst[Counter]
      Profit = Selling_Price - Buying_Price
      
      if (Profit <= 0) or (Profit <= Maximum_Profit):
        Cursor += 1
      else:
        Maximum_Profit = Profit
        Cursor += 1
    
    Counter += 1
    
  return Maximum_Profit

