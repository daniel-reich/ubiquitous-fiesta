
def hours_passed(time1, time2):
  if time1 == time2:
    return 'no time passed'
  elif 'AM' in time1 and 'PM' in time2:
    return '{} hours'.format(abs(int(time1.split(':')[0])-12) + int(time2.split(':')[0]))
  elif 'AM' in time1 and 'AM' in time2:
    return '{} hours'.format(abs(int(time1.split(':')[0]) - int(time2.split(':')[0])))
  elif 'PM' in time1 and 'PM' in time2:
    return '{} hours'.format(abs(int(time1.split(':')[0]) - int(time2.split(':')[0])))

