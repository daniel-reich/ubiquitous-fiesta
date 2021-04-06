
def hours_passed(time1, time2):
  time1AM = time1[-2:]
  time2AM = time2[-2:]
  colonIndx1 = time1.index(":")
  colonIndx2 = time2.index(":")
  hour1 = time1[:colonIndx1]
  hour2 = time2[:colonIndx2]
  hour1 = int(hour1)
  hour2 = int(hour2)
  #print(time1AM, time2AM)
  if time1AM == "AM":
    if hour1 == 12:
      hour1 = 0
    #print(hour1)
  else:
    if hour1 == 12:
      hour1 = 12
    else:
      hour1 += 12
  if time2AM == "AM":
    if hour2 == 12:
      hour2 = 0
    #print(hour1)
  else:
    if hour2 == 12:
      hour2 = 12
    else:
      hour2 += 12
  if hour2-hour1==0:
    return "no time passed"
  else:
    return str(hour2-hour1) + " hours"

