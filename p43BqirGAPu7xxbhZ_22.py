
import math
def diamond(carat):
  row = carat - 1 if carat % 2 == 0 else carat
  r = row // 2
  c2 = carat // 2
  c1 = c2 if carat % 2 == 1 else c2-1
  diamond = [[0 for j in range(0,carat)]for i in range(0,row)]
  diamond[r][0] = 1
  diamond[r][carat-1] = 1
  status = "good cut" if carat % 2 == 0 else "perfect cut"
  for i in range(0,r):
    diamond[i][c2+i] = 1
    diamond[i][c1-i] = 1
    diamond[row-1-i][c1-i] = 1
    diamond[row-1-i][c2+i] = 1
  return [diamond,status]

