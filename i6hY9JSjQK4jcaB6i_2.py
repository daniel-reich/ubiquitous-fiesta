
def color_invert(rgb):
  rgb_lst = list(rgb)
  re = []
  for i in rgb_lst:
    re.append(255-i)
  return tuple(re)

