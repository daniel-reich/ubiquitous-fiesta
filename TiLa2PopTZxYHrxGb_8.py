
def playback_duration(duration, speed):
  t = [int(x) for x in duration.split(":")]
  t_sec = (t[0] * 3600 + t[1]* 60 + t[2]) / speed
  h = int(t_sec//3600)
  m = int(t_sec%3600 // 60)
  s = int(t_sec%3600 % 60)
  return "{:0>2}:{:0>2}:{:0>2}".format(h, m, s)

