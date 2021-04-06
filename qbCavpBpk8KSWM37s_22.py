
def largest_gap(lst):
  
  Sample = sorted(lst)
  
  Highest = 0
  First = 0
  Second = 1
  Length = len(lst)
  
  while (Second < Length):
    Item_B = Sample[Second]
    Item_A = Sample[First]
    Score = Item_B - Item_A
    
    if (Score > Highest):
      Highest = Score
      First += 1
      Second += 1
    else:
      First += 1
      Second += 1
  
  return Highest

