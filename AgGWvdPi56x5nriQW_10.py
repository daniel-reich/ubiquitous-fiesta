
def longest_slide(pyramid):
  for i in range(len(pyramid) - 2, -1, -1):
    for j in range(len(pyramid[i])):
      pyramid[i][j] += max(pyramid[i + 1][j], pyramid[i + 1][j + 1])
  return pyramid[0][0]

