
def bonus(days):
​
  pay = 0
​
  if days > 0:
    if days < 32:
      pay += (days * 0)
    else:
      pay += (32 * 0)
    
    if days > 32:
      if days < 40:
        pay += ((days - 32) * 325)
      else:
        pay += (8 * 325)
      
      if days > 40:
        if days < 48:
          pay += ((days - 40) * 550)
        else:
          pay += (8 * 550)
        
        if days > 48:
          pay += ((days - 48) * 600)
  
  return pay

