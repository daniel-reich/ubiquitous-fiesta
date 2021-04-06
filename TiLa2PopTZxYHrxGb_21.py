
def playback_duration(duration, speed):
  hour, minute, second = map(int, duration.split(":"))
  total = hour*3600 + minute*60 + second
  total /= speed
  hours = int(total // 3600)
  total -= hours*3600
  minutes = int(total // 60)
  total -= minutes*60
  seconds = int(total)
  return "{:0>2}:{:0>2}:{:0>2}".format(hours, minutes, seconds)

