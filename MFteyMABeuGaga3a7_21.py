
def color_pattern_times(cols):
  switches = sum(cols[i] != cols[i-1] for i in range(1,len(cols)))
  return len(cols) * 2 + switches

