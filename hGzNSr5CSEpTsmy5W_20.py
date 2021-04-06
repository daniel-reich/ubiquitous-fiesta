
def not_good_math(Number, Steps):
  
  Performed = 0
  
  while (Performed < Steps):
    
    Text = str(Number)
    
    if (Text[-1] == "0"):
      Text = Text[0:-1]
      Number = int(Text)
      Performed += 1
    else:
      Number -= 1
      Performed += 1
  
  return Number

