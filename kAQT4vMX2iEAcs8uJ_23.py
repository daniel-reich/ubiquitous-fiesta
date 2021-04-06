
def longest_7segment_word(lst):
  
  Eligible = []
  Spans = []
  
  Counter = 0
  Length = len(lst)
  
  while (Counter < Length):
    
    Thing = lst[Counter]
    Item = Thing.upper()
    Span = len(Item)
    
    if ("K" in Item):
      Counter += 1
    elif ("M" in Item):
      Counter += 1
    elif ("V" in Item):
      Counter += 1
    elif ("W" in Item):
      Counter += 1
    elif ("X" in Item):
      Counter += 1
    else:
      Eligible.append(Thing)
      Spans.append(Span)
      Counter += 1
  
  if (Eligible == []):
    return ""
  
  Longest = max(Spans)
  
  Counter = 0
  Length = len(Eligible)
  
  while (Counter < Length):
    
    Word = Eligible[Counter]
    Distance = len(Word)
    
    if (Distance == Longest):
      return Word
    else:
      Counter += 1

