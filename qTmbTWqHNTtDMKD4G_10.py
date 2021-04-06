
def get_path_length(world, width, height):
  INF = width*height + 1
  world = ['t'*(width+2)] + [['t'] + world.split(',')[i*width:(i+1)*width] + ['t'] for i in range(height)] + ['t'*(width+2)]
  for i in range(1, height+1):
    for j in range(1, width+1):
      if world[i][j] == 'm':
        mi, mj = i, j
      if world[i][j] == 'h':
        hi, hj = i, j
  dist = [[INF]*(width+2) for _ in range(height+2)]
  dist[mi][mj] = 0
  for _ in range((width+2)*(height+2)+1):
    for i in range(1, height+1):
      for j in range(1, width+1):
        if world[i][j] != 't':
          dist[i][j] = min(dist[i+dy][j+dx]+(dx!=0 or dy!=0) for dx in (-1,0,1) for dy in (-1,0,1))
  return -1 if dist[hi][hj]==INF else dist[hi][hj]

