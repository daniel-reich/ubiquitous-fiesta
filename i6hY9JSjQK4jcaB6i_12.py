
def color_invert(rgb):
  return tuple(abs(255-int(i)) for i in list(rgb))

