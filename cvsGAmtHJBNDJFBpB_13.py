
def can_traverse(x):
  heights = []
  for y in range(len(x[0])):
    add = 0
    for row in x:
      if row[y] == 1:
        add += 1
    heights.append(add)
  for y in range(len(heights) - 1):
    if abs(heights[y + 1] - heights[y]) > 1:
      return False
  return True

