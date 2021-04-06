
def switch_gravity_on(blocks):
  x = len(blocks[0])
  y = len(blocks)
​
  for r in range(y):
      for i in range(x):
          for a in range(y - 2, -1, -1):
              if blocks[a + 1][i] == '-' and blocks[a][i] == '#':
                  blocks[a + 1][i] = "#"
                  blocks[a][i] = "-"
  return blocks

