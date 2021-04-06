
def color_pattern_times(cols):
  time = len(cols) * 2
  for i in range(len(cols) - 1):
    if cols[i] != cols[i + 1]:
      time += 1
  return time

