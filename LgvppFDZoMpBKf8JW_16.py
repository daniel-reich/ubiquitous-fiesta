
def digital_clock(seconds):
  minutes = (seconds // 60) % 60
  hours = (seconds // 3600) % 24
  seconds %= 60
  return '{:02}:{:02}:{:02}'.format(hours, minutes,seconds)

