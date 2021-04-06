
def color_pattern_times(cols):
  return len(cols)*2 + sum(1 for i in range(len(cols)-1) if cols[i] != cols[i+1])

