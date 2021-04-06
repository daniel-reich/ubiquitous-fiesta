
def harry(po):
  sy, sx = len(po), len(po[0])
  if sx == 0: return -1
  
  dp = [0] * (sy * sx)
  dp[0] = po[0][0]
  
  for y in range(0, sy):
    for x in range(0, sx):
      n = [po[y][x]]
      if y: n.append(dp[(y-1) * sx + x] + po[y][x])
      if x: n.append(dp[y * sx + (x-1)] + po[y][x])
      dp[y * sx + x] = max(n)
​
  return dp.pop()

