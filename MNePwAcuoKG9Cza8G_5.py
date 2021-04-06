
def build_staircase(height, block):
  a = []
  for i in range(height):
    a.append([block] * (i + 1) + ['_'] * (height - i - 1))
  return a

