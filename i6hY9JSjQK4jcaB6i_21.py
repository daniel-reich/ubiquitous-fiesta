
def color_invert(rgb):
  result_list = []
  rgb_list = list(rgb)
  for n in rgb_list:
    result_list.append(255-n)
  return tuple(result_list)

