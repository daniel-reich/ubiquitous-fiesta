
def number_length(num):
  
  if (num < 10):
    return 1
  else:
    Total = 0
    Power = 0
    Addition = 9 * (10 ** Power)
    Length = 0
    
    while (Total < num):
      Total += Addition
      Length += 1
      Power += 1
      Addition = 9 * (10 ** Power)
      
    return Length

