
def diagonalize(n, d):
  mat = []
  for i in range(n):
    mat.append([])
    for j in range(n):
      mat[i].append(0)
  if d == 'ul':
    startX = 0
    startY = 0
    dirX = 1
    dirY = 1
  elif d == 'ur':
    startX = n - 1
    startY = 0
    dirX = -1
    dirY = 1
  elif d == 'll':
    startX = 0
    startY = n - 1
    dirX = 1
    dirY = -1
  elif d == 'lr':
    startX = n - 1
    startY = n - 1
    dirX = -1
    dirY = -1
  num = 0
  YPos = startY
  for i in range(n):
    XPos = startX
    tnum = num
    for j in range(n):
      mat[YPos][XPos] = tnum
      tnum += 1
      XPos += dirX
    YPos += dirY
    num += 1
  return mat

