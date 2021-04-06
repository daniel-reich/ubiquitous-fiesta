
def hours_passed(time1, time2):
  
  class Time:
    
    def __init__(self, hours, mins, ap):
      self.h = hours
      self.m = mins
      self.ap = ap
    
    def hours_passed(self, other):
      if self.ap == 'AM' and other.ap == 'PM':
        return (12 - self.h) + other.h
      elif self.ap == 'PM' and other.ap == 'AM':
        return (12 - other.h) + self.h
      else:
        hours = [self.h, other.h]
        print(hours)
        return max(hours) - min(hours)
  
  t1, ap1 = time1.split()
  h1, m1 = [int(i) for i in t1.split(':')]
  
  t2, ap2 = time2.split()
  h2, m2 = [int(i) for i in t2.split(':')]
  
  time1 = Time(h1, m1, ap1)
  time2 = Time(h2, m2, ap2)
  
  hd = time1.hours_passed(time2)
  
  if hd == 0:
    return 'no time passed'
  elif hd == 1:
    return '1 hour'
  else:
    return '{} hours'.format(hd)

