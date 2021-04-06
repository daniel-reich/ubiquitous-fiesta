
def lets_meet(distance, va, vb):
  tym = distance/(va+vb) *3600
  hour = tym//3600
  minutes = (tym/3600 - hour)*60
  sec = (minutes - int(minutes))*60
  return '{}h {}min {}s'.format(int(hour), int(minutes), int(sec))

