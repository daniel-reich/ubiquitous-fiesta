
def color_pattern_times(cols):
​
  if (cols == []):
    return 0
​
  Blocks = cols
  
  Time = 2
  
  Previous = 0
  Current = 1
  Length = len(Blocks)
  
  while (Current < Length):
    
    Item_A = Blocks[Previous]
    Item_B = Blocks[Current]
    
    if (Item_B == Item_A):
      Time += 2
      Previous += 1
      Current += 1
    else:
      Time += 3
      Previous += 1
      Current += 1
  
  return Time

