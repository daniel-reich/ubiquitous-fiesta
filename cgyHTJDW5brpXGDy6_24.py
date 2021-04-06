
def parse_time(time):
  c1 = time.find(':')
  c2 = time.rfind(' ')
  hours = int(time[:c1])
  minutes = int(time[c1+1:c2])
  modifier = time[c2+1:]
  if modifier == 'PM':
    hours += 12
  return hours
​
def hours_passed(time1, time2):
  if time1 == time2:
    return 'no time passed'
  return str(parse_time(time2) - parse_time(time1))+' hours'

