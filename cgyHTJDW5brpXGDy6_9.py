
def hours_passed(time1, time2):
  a, b = map(lambda x: eval(''.join(x.split(':00 ')).replace('PM', '+12').replace('AM', '')), [time1, time2])
  return '{} hours'.format(b - a) if b - a else 'no time passed'

