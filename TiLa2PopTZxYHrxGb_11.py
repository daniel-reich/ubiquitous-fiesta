
from math import floor
​
def playback_duration(duration, speed):
  h, m, s = map(int, duration.split(':'))
  secs = h*3600 + m*60 + s
  playback = floor(secs / speed)
  
  h, m = divmod(playback, 3600)
  m, s = divmod(m, 60)
  return '{:02}:{:02}:{:02}'.format(h, m, s)

