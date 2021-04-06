
def playback_duration(d, sp):
  h, m, s = map(int, d.split(':'))
  s = int((s + m * 60 + h * 3600) / sp)
  return '{:02d}:{:02d}:{:02d}'.format(s // 3600, (s // 60) % 60, s % 60)

