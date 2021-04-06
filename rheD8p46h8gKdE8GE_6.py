
def grayscale(lst):
  isGrey = lambda a: all([a[0]==x for x in a])
  prep = lambda a: [255 if x>255 else (0 if x<0 else x) for x in a]
  makeGrey = lambda a: [round(sum(a)/len(a)) for x in a]
  return [[pixels if isGrey(pixels) else makeGrey(prep(pixels))
          for pixels in pic]
            for pic in lst]

