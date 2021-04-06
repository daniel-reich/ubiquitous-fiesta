
def playback_duration(duration, speed):
  hrs,mins,secs = map(int,duration.split(':'))
  t = int((hrs*3600+mins*60+secs)//speed)
  h,t = divmod(t,3600)
  m,s = divmod(t,60)
  return '{:02d}:{:02d}:{:02d}'.format(h,m,s)

