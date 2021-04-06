
def hours_passed(time1, time2):
  if time1 == time2:
    return 'no time passed'
  elif 'AM' in time1 and 'PM' in time2:
    onetime = int(time1.split(':')[0])
    twotime = int(time2.split(':')[0])
    if onetime == 12:
      return '{} hours'.format(12 + twotime)
    else:
      return '{} hours'.format(12 + abs(onetime - twotime))
  elif 'AM' in time1 and 'AM' in time2:
    onetime = int(time1.split(':')[0])
    twotime = int(time2.split(':')[0])
    return '{} hours'.format(abs(twotime - onetime))
  elif 'PM' in time1 and 'PM' in time2:
    onetime = int(time1.split(':')[0])
    twotime = int(time2.split(':')[0])
    return '{} hours'.format(abs(twotime - onetime))

