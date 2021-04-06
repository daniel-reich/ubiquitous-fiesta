
def classify_rug(pattern):
  def is_same(a, b):
    return a == b
  def flip_vertically(a):
    result = []
    for row in a:
      result.append(row[::-1])
    return result
  height, width = len(pattern), len(pattern[0])
  if height == 1 and width == 1:
    return 'perfect'
  is_horizontally_symmetric = is_same(pattern, pattern[::-1])
  is_vertically_symmetric = is_same(pattern, flip_vertically(pattern))
  if is_horizontally_symmetric and is_vertically_symmetric:
    return 'perfect'
  elif is_horizontally_symmetric:
    return 'horizontally symmetric'
  elif is_vertically_symmetric:
    return 'vertically symmetric'
  else:
    return 'imperfect'

