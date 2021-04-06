
def hex_color_mixer(colors):
  mix = '#'
  for i in range(1, 7, 2):
      mix += hex(round((sum([int(cx[i:i+2], 16) for cx in colors]) / len(colors)) + 0.00001)).upper()[2:].zfill(2)
  return mix

