
def bonus(days):
  second,third,fourth = 0,0,0
  for num in range(1,days+1):
    if num in range(33,41):
      second += 1
    elif num in range(41,49):
      third += 1
    elif num > 48:
      fourth += 1
      
  return second*325 + third*550 + fourth*600 + 0

