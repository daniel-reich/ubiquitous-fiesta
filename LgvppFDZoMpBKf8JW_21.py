
def digital_clock(seconds):
  h = (seconds // 3600)
  m = (seconds % 3600) // 60
  s = seconds - (h * 3600 + m * 60)
  h = h % 24
  return '{:02d}:{:02d}:{:02d}'.format(h, m, s)

