
def can_traverse(x):
  heights = []
  for c in range(len(x[0])):
    height = 0
    for r in range(len(x)):
      if x[r][c] == 1:
        height += 1
    heights.append(height)
  for i in range(len(heights)-1):
    if abs(heights[i] - heights[i+1]) > 1:
      return False
  return True

