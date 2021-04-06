
def longest_slide(pyramid):
  for r in range(len(pyramid)-2, -1, -1):
    for c in range(len(pyramid[r])):
      pyramid[r][c] += max(pyramid[r+1][c], pyramid[r+1][c+1])
  return pyramid[0][0]

