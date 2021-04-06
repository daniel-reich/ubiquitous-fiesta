
def classify_rug(pattern):
  transposed = list(map(list, zip(*pattern)))
  horizontal = all([pattern[x]==pattern[-x-1] for x in range(len(pattern))])
  vertical = all([transposed[x]==transposed[-x-1] for x in range(len(transposed))])
  if horizontal and vertical:
    return "perfect"
  elif horizontal:
    return "horizontally symmetric"
  elif vertical:
    return "vertically symmetric"
  else:
    return 'imperfect'

