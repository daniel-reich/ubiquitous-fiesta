
def microwave_buttons(time):  
  if time == '00:00':
    return 1
  if time == '00:30':
    return 2
  if time[0:2] == '00' or int(time[0:2]) < 10:
    return 3
  if int(time[0:2]) >= 10:
    return 5

