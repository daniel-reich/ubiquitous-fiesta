
def most_expensive_item(products):
  
  Things = []
  
  for x in products.keys():
    Things.append(x)
  
  Worth = []
  
  for y in products.values():
    Worth.append(y)
    
  Highest = max(Worth)
  
  Counter = 0
  Length = len(Things)
  
  while (Counter < Length):
    Item = Things[Counter]
    Money = Worth[Counter]
    
    if (Money == Highest):
      return Item
    else:
      Counter += 1

