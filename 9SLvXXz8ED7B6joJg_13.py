
def lets_meet(distance, va, vb):
  time = distance / (va + vb)
  hours = int(time // 1)
  minutes = int(((time % 1) * 60) // 1)
  seconds = int((((time % 1) * 60) % 1) * 60)
  return "{}h {}min {}s".format(hours, minutes, seconds)

