
def weekly_salary(hours):
  tally = 0
  
  for i in range(0,len(hours)):
    if i >= 0 and i <=4:
      #weekday
      if hours[i] <= 8:
        tally += hours[i]*10
      else : 
        tally += 8 * 10
        tally += (hours[i]-8)*15
    else : 
      #weekend
      if hours[i] <= 8:
        tally += hours[i]*20
      else : 
        tally += 8 * 20
        tally += (hours[i]-8)*30
  return tally

