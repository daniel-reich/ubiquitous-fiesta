
def playback_duration(duration, speed):
  h, m, s = map(int, duration.split(":"))
  t = int((h * 3600 + m * 60 + s) / speed)
  return "{:02d}:{:02d}:{:02d}".format(t // 3600, t // 60 % 60, t % 60)

