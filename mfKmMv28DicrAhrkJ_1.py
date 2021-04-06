
def hex_color_mixer(colors):
  n = len(colors)
  r = sum([int(c[1:3], 16) for c in colors]) / n
  g = sum([int(c[3:5], 16) for c in colors]) / n
  b = sum([int(c[5:], 16) for c in colors]) / n
  return '#{:0<2X}{:0<2X}{:0<2X}'.format(int(r + 0.5), int(g + 0.5), int(b + 0.5))

