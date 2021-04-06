
def hours(time):
  c = time.find(':')
  hours = int(time[:c])%12
  mod = time[-2:]
  if mod == 'PM':
    hours += 12
  return hours
​
def hours_passed(time1, time2):
  if time1 == time2:
    return 'no time passed'
  return str(hours(time2)-hours(time1)) + ' hours'

