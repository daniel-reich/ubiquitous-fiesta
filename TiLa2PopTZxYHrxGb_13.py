
from math import floor
string = lambda x: '0' + str(x) if x < 10 else str(x)
def playback_duration(duration, speed):
  time = duration.split(':');
  seconds = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
  seconds /= speed
  hours = floor(seconds / 3600)
  seconds -= 3600 * hours
  minutes = floor(seconds / 60)
  seconds -= 60 * minutes
  seconds = floor(seconds)
  return '{}:{}:{}'.format(string(hours),string(minutes),string(seconds))

