
def grayscale(lst):
  for row in lst:
    for pixel in row:
        pixel[:] = [max(min(p, 255),0) for p in pixel]
        pixel[:] = [int(round(sum(pixel)/len(pixel)))] * len(pixel)
  return lst

