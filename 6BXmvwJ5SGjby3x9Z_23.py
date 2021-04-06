
def hours_passed(time1, time2):
  if time1 == time2: return "no time passed"
  
  h1 = int(time1.split(':')[0])
  h2 = int(time2.split(':')[0])
  
  if time1 == '12:00 AM': h1=0
  if 'PM' in time1:
    if h1 == 12: h1=12
    else: h1+=12
  
  if time2 == '12:00 AM': h2=0
  if 'PM' in time2:
    if h2 == 12: h2=12
    else: h2+=12
  
  return str(h2-h1) + ' hours'

