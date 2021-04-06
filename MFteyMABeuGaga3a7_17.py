
def color_pattern_times(cols):
  if not len(cols): return 0
  secs = 0
  color = cols[0]
  for i in cols:
    secs += 2
    if i != color:
      secs += 1
    color = i
  return secs

