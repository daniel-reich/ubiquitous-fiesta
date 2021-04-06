
def digital_clock(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 60 * 60) // 60
  seconds = int(seconds - (hours * 60 * 60 + minutes * 60))
  return '{:0>2}:{:0>2}:{:0>2}'.format(
    hours % 24,
    minutes % 60,
    seconds % 60
  )

