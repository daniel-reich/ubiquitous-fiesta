
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
​
def on_grid(width, height, r, c):
    return r >= 0 and c >= 0 and r < height and c < width
    
def get_path_length(world, width, height):
  world = [[world.split(',')[r*width + c] for c in range(width)] for r in range(height)]
  que = []
  for r in range(height):
    for c in range(width):
      if world[r][c] == 'm':
        que.append((r, c))
        world[r][c] = 0
        break
  while que:
    r, c = que.pop(0)
    for dir in dirs:
      r2, c2 = r+dir[0], c+dir[1]
      if on_grid(width, height, r2, c2):
        if world[r2][c2] == '.':
          world[r2][c2] = world[r][c] + 1
          que.append((r2, c2))
        elif world[r2][c2] == 'h':
          return world[r][c] + 1
  return -1

