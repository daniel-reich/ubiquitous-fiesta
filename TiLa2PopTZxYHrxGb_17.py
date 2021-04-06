
def playback_duration(d, s):
  t = int(eval("({}*3600)+({}*60)+{}".format(*[int(i) for i in d.split(':')]))/s)
  return "{:02d}:{:02d}:{:02d}".format(t//3600, t%3600//60, t%3600%60)

