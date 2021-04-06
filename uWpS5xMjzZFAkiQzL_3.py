
def odds_vs_evens(num):
  sumOdd = 0
  sumEven = 0
  numStr = str(num)
  
  for i in numStr:
    x = int(i)
    
    if x % 2 == 0:
      sumEven = sumEven + x
    else:
      sumOdd = sumOdd + x
      
  if sumEven > sumOdd:
    return "even"
  elif sumOdd > sumEven:
    return "odd"
  else:
    return "equal"

