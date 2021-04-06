
def hours_passed(time1, time2):
  if time1 == time2: return "no time passed" 
  
  h1 = int(time1[:time1.index(':')])
  h2 = int(time2[:time2.index(':')])
  
  if 'PM' in time1: 
    h1+=12
  if 'PM' in time2:
    h2+=12
  
  if h1 == 12: h1 = 0
  if h2 == 12: h2 = 0
​
  return str(h2-h1) + ' hours'

