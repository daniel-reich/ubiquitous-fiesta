
import re
def playback_duration(duration, speed):
  h,m,s = map(int,re.findall("\d+",duration))
  x = int((h*3600+m*60+s)/speed)
  return "{:0>2}:{:0>2}:{:0>2}".format(x//3600,x%3600//60,x%60)

