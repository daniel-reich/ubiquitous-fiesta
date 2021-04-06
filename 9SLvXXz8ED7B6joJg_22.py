
def lets_meet(distance, va, vb):
  x = distance / (va+vb)
  hours = int(x)
  x = (x - hours) * 60
  mins = int(x)
  x = (x - mins) * 60
  secs = int(x)
  return "{}h {}min {}s".format(str(hours), str(mins), str(secs))

