
def turn_calc(num):
  
  CODE = {"1" : "I", "2" : "Z", "3" : "E", "4" : "H", "5" : "S", 
          "6" : "G", "7" : "L", "8" : "B", "9" : "-", "0" : "O"}
​
  Decoded = ""
  Sample = str(num)       
  
  Counter = 0
  Length = len(Sample)
  
  while (Counter < Length):
    Item = str(Sample[Counter])
    
    if (Item == "."):
      Counter += 1
    
    else:
      Letter = CODE[Item]
      Decoded = Letter + Decoded
      Counter += 1
  
  return Decoded

