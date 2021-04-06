
def color_pattern_times(cols):
  if cols==[]: return 0
  time = 2
  for i in range(1, len(cols)):
    if cols[i] != cols[i-1:][0]:
      time += 3
    else:
      time += 2
  return time

