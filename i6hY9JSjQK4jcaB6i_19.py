
def color_invert(rgb):
  return tuple([
    abs(color - 255)
    for color in rgb
  ])

