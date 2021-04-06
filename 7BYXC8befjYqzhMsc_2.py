
def classify_rug(pattern):
  vertical = pattern == [i[::-1] for i in pattern]
  horizontal = list(zip(*pattern)) == [i[::-1] for i in zip(*pattern)]
  
  if horizontal and vertical:
    return 'perfect'
  if horizontal:
    return 'horizontally symmetric'
  if vertical:
    return 'vertically symmetric'
  return 'imperfect'

