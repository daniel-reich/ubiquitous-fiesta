
def hours_passed(t1, t2):
  if t1 == t2:
    return 'no time passed'
  a = halp(t1)
  b = halp(t2)
  if b < a:
    b += 24
  return '{} hours'.format((b-a))
  
def halp(time):
  a, b = time.split()
  a, _ = a.split(':')
  if a == '12' and b == 'AM':
    a = '0'
  return int(a) + 12*(b=='PM')

