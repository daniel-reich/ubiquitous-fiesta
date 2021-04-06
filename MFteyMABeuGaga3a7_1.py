
def color_pattern_times(cols):
  return len(cols)*2 + sum(i != j for i, j in zip(cols[1:], cols))

