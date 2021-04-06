
def conv(time):
  return int(time.split(':')[0]) + (12 if time[-2]=='P' or time[:2]=='12' else 0)
​
def hours_passed(time1, time2):
  delta = (conv(time2) - conv(time1))%24
  return '{} hours'.format(delta) if delta else 'no time passed'

