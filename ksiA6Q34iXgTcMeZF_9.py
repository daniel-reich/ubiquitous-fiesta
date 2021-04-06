
def bonus(days):
  inct = 0
  if(days > 48) :
    d = days - 48
    inct = d * 600 + 7000
  elif(days > 40) :
    d = days - 40
    inct = d * 550 + 2600
  elif(days > 32) :
    d = days - 32
    inct = d * 325 + 0
     
  return inct

