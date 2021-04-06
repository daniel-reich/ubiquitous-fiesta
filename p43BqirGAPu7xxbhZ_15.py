
def diamond(carat):
  width = carat // 2 + carat % 2
  diamond = [[0 for i in range(width)] for i in range(width)]
  for i in range(width):
    diamond[i][i] = 1
  if carat%2 == 0:
    diamond = [row[::-1] + row for row in diamond]
  else:
    diamond = [row[:0:-1] + row for row in diamond]
  diamond += [diamond[i] for i in range(width-2, -1, -1)]
  return [diamond, 'perfect cut' if carat % 2 else 'good cut']

