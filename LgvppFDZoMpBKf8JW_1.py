
import time
​
def digital_clock(seconds):
  return time.strftime("%H:%M:%S", time.gmtime(seconds))

