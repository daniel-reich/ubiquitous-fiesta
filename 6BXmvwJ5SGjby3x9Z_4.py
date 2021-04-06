
def hours_passed(time1, time2):
  if time1==time2: return "no time passed"
  a, b = time1.split()
  c, d = time2.split()
  h1 = int(a[:-3])
  h2 = int(c[:-3])
  e = (h1+12)%24 if (b=="PM" and h1!=12) or (b=="AM" and h1==12)\
      else h1
  f = (h2+12)%24 if (d=="PM" and h2!=12) or (d=="AM" and h2==12)\
      else h2
  return '{} hours'.format(f - e)

