
def grayscale(lst):
  for layer in lst:
    for pixel in layer:
      for i in [0,1,2]:
        if pixel[i] < 0:
          pixel[i] = 0
        if pixel[i] > 255:
          pixel[i] = 255
      grey = round((pixel[0]+pixel[1]+pixel[2])/3)
      pixel[0],pixel[1],pixel[2] = grey,grey,grey
  return lst

