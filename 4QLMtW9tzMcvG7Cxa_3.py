
def resistance_calculator(resistors):
  
  Top_Part_01 = 1
  Top_Part_02 = 0
  Bottom = 0
   
  Counter = 0
  Length = len(resistors)
  
  if (Length == 2):
        
    Parallel = (resistors[0] * resistors[1]) / (resistors[0] + resistors[1])
    Parallel = round(Parallel,2)
    Series = sum(resistors)
    Series = round(Series,2)
    
    Answer = []
    Answer.append(Parallel)
    Answer.append(Series)
  
    return Answer
  
​
  else:
    
    while (Counter < Length):
            
      Item = resistors[Counter]
            
      if (Item == 0):
        Value = 0
        Top_Part_02 += Value
        Bottom += Item
                        
      else:
        Value = 1 / Item
        Top_Part_02 += Value
        Bottom += Item      
            
      Counter += 1
            
    if (Top_Part_02 == 0):
      Parallel = 0
​
    else:
      Parallel = round(Top_Part_01 / Top_Part_02,2)
        
    Series = sum(resistors)
    Series = round(Series,2)
  
    Answer = []
    Answer.append(Parallel)
    Answer.append(Series)
  
    return Answer

