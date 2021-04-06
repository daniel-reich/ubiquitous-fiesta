
def color_pattern_times(cols):
  changes = sum(a != b for a, b in zip(cols, cols[1:]))
  return changes + len(cols)*2

