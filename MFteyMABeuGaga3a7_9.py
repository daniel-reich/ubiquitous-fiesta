
def color_pattern_times(cols):
  if len(cols) == 0:
    return 0
  time = 0
  x = cols[0]
  for y in cols:
    if x != y:
      time = time + 1
    time = time + 2
    x = y
  return time

