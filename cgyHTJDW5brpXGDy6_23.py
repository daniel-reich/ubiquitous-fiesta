
def hours_passed(time1, time2):
  if time1 == time2: return 'no time passed'
  t1, m1 = int(time1.split(':')[0]), time1[-2:]
  t2, m2 = int(time2.split(':')[0]), time2[-2:]
  if t1 < 12 and m1 == 'PM':
    t1 += 12
  if t2 < 12 and m2 == 'PM':
    t2 += 12
  return '{} hours'.format(abs(t1-t2))

