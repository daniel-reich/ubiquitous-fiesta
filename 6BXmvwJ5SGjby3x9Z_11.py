
def hours_passed(time1, time2):
  if time1 == '12:00 AM':
    a = 0
  else:
    a = int(time1.split(':')[0])
  b = int(time2.split(':')[0])
  if time1.endswith('PM'):
    a+=12
  if time2.endswith('PM'):
    b+=12
  return str(b-a)+' hours' if a!=b else 'no time passed'

