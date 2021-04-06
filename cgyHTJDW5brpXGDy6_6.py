
def hours_passed(time1, time2):
  if time1[-2:] == 'PM':
    t1 = int(time1[0]) + 12
  else:
    t1 = int(time1[0])
  if time2[-2:] == 'PM':
    t2 = int(time2[0]) + 12
  else:
    t2 = int(time2[0])
  if t2 == t1:
    return "no time passed"
  return str(t2-t1) + ' hours'

