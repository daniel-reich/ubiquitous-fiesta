
def microwave_buttons(time):
  mins = int(time[0:2])
  secs = int(time[3:5])
  
  total_time = (mins * 60) + secs 
  
  thirty_presses = total_time // 30
  if total_time % 30 > 0:
    if total_time % 30 < 10:
      thirty_presses += 1
    else:
      thirty_presses += 2
  
  ind_presses = 0
  if mins > 0:
    if mins > 9:
      ind_presses = 4
    else:
      ind_presses = 3
  if ind_presses == 0:
    if secs > 9:
      ind_presses = 2
    else:
      ind_presses = 1
  
  if thirty_presses < ind_presses:
    return thirty_presses + 1
  else:
    return ind_presses + 1

