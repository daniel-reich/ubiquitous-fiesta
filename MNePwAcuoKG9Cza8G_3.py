
def build_staircase(height, block):
  stairs = []
  for i in range(1, height+1):
    stair = [block] * i + ['_'] * (height - i)
    stairs.append(stair)
  return stairs

