
def color_invert(rgb):
  arr=[]
  for r in rgb:
    if r-255<0:
      arr.append(-(r-255))
    else:
      arr.append(r-255)
  return tuple(arr)

