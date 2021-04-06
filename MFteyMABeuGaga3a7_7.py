
def color_pattern_times(cols):
  return len(cols)*2 + sum([1 for x in range(0, len(cols)-1) if cols[x] != cols[x+1]])

