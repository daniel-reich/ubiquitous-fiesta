
def lets_meet(distance, va, vb):
  totalSeconds = 3600 * distance / (va + vb)
  hours = int(totalSeconds // 3600)
  minutes = int((totalSeconds%3600)//60)
  seconds = int((totalSeconds%3600)%60)
  return "{}h {}min {}s".format(hours, minutes, seconds)

