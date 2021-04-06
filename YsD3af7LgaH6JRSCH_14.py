
def time_adjust(now, hrs, mins, secs):
  
  h,m,s = [int(t) for t in now.split(':')]
​
  s,r = (secs + s) % 60, (secs + s) // 60
  m,r = (mins + m + r) % 60 , (mins + m + r) // 60
  h = (hrs + h + r) % 24
​
  return '{:0>2}:{:0>2}:{:0>2}'.format(h,m,s)

