
def color_pattern_times(colors):
  if colors == []:
    return 0
  return sum([2 if color == colors[idx] else 3 for idx, color in enumerate(colors[1:])]) + 2

