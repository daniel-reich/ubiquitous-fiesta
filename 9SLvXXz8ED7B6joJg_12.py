
def lets_meet(distance, va, vb):
  time = distance/(va+vb)
  mins = (time-int(time))*60
  sec = (mins-int(mins))*60
  return "{}h {}min {}s".format(int(time),int(mins),int(sec))

