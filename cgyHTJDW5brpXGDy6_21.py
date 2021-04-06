
def hours_passed(time1, time2):
  if time1==time2:
    return 'no time passed'
  a,b = int(time1.split(':')[0]),int(time2.split(':')[0])
  if time1.endswith('PM'):
    a+=12
  if time2.endswith('PM'):
    b+=12
  return str(b-a)+' hours'

