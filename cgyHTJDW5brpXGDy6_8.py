
def hours_passed(time1, time2):
  h1, p1 = time1.split(':')
  h2, p2 = time2.split(':')
  h1 = int(h1) + (12 if p1[-2:] == 'PM' else 0)
  h2 = int(h2) + (12 if p2[-2:] == 'PM' else 0)
  diff = abs(h2 - h1)
  return '{} hours'.format(diff) if diff != 0 else 'no time passed'

