
def hours_passed(time1, time2):
  if 'PM' in time1: time1=int(time1[:-6])+12
  elif 'AM' in time1: time1=int(time1[:-6])
  if 'PM' in time2: time2=int(time2[:-6])+12
  elif 'AM' in time2: time2=int(time2[:-6])
  if time2-time1==0: return 'no time passed'
  return str(time2-time1)+' hours'

