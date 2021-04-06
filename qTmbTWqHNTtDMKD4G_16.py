
def get_path_length(world, width, height):
  world = world.split(',')
  world = [world[i:i+width] for i in range(0,len(world),width)]
  for y in range(len(world)):
    for x in range(len(world[y])):
      if world[y][x] == 'm':
        start = [y,x]
        world[y][x] = 0
      elif world[y][x] == 't':
        world[y][x] = -2
      elif world[y][x] == 'h':
        end = [y,x]
        world[y][x] = -1
      else:
        world[y][x] = -1
  val = 0
  y,x = start
  nodes = [[y,x+1],[y,x-1],[y+1,x],[y-1,x],[y+1,x+1],[y+1,x-1],[y-1,x+1],[y-1,x+1]]
  nodes = [i for i in nodes if 0<=i[0]<len(world) and 0<=i[1]<len(world[i[0]]) and world[i[0]][i[1]] != -2]
  while any([world[a][b] == -1 for a,b in nodes]):
    new_nodes = []
    for i in nodes:
      a,b = i
      if world[a][b] == -1:
        world[a][b] = val+1
      new_nodes += [[a,b+1],[a,b-1],[a+1,b],[a-1,b],[a+1,b+1],[a+1,b-1],[a-1,b+1],[a-1,b-1]]
    val+=1
    new_nodes = [i for i in new_nodes if 0<=i[0]<len(world) and 0<=i[1]<len(world[i[0]]) and world[i[0]][i[1]] != -2]
    nodes = []
    for i in new_nodes:
      if i not in nodes:
        nodes.append(i)
  return world[end[0]][end[1]]

