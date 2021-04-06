
def half_a_fraction(fract):
  
  Sample = str(fract)
  Blocks = Sample.split("/")
  
  Top = int(Blocks[0])
  Bottom = int(Blocks[1])
  Bottom *= 2
  
  Target = 1
  Counter = 1
  
  while (Counter <= Top):
    
    if (Top % Counter == 0) and (Bottom % Counter == 0):
      Target = int(Counter)
      Counter += 1
    else:
      Counter += 1
    
  Top /= Target
  Top = int(Top)
  
  Bottom /= Target
  Bottom = int(Bottom)
  
  Answer = str(Top) + "/" + str(Bottom)
  
  return Answer

