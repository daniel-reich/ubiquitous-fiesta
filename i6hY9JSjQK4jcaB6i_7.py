
def color_invert(rgb):
  a = (255, 255, 255)
  return tuple(a[i] - rgb[i] for i in range(len(a)))

