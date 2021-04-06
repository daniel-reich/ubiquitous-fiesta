
def bed_time(*times):
  return [get_bed_time(*i) for i in times]
  
def get_bed_time(wakeup, duration):
  wh, wm = map(int, wakeup.split(':'))
  dh, dm = map(int, duration.split(':'))
  h, m = wh - dh, wm - dm
  
  return '{:02d}:{:02d}'.format((h - (m < 0)) % 24, m % 60)

