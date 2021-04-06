
def lets_meet(distance, va, vb):
  time = distance / (va + vb)
  hours = time // 1
  minutes = (time - hours) * 60
  sec = (minutes - minutes//1) * 60
  minutes = minutes // 1
  return "{}h {}min {}s".format(int(hours), int(minutes), int(sec))

