
def expand(center, visited, width, height):
  fields = []
  cx, cy = center
  for x in range(max(0, cx - 1), min(width - 1, cx + 1) + 1): 
    for y in range(max(0, cy - 1), min(height - 1, cy + 1) + 1):
      if not visited[x][y]:
        visited[x][y] = True
        fields.append((x,y))
  return fields
​
def get_path_length(world, width, height):
  visited = [[False for y in range(height)] for x in range(width)]
  world = world.replace(',', '')
  i = 0
  for x in range(width):
    for y in range(height):
      if world[i] == 'm':
        start = (x, y)
        visited[x][y] = True
      elif world[i] == 'h':
        goal = (x, y)
      elif world[i] == 't':
        visited[x][y] = True
      i += 1
​
  dist = 0
  neighbours = [start]
  while neighbours:
    dist += 1
    expanded = []
    for n in neighbours:
      expanded.extend(expand(n, visited, width, height))
    if goal in expanded:
      return dist
    neighbours = expanded
    
  return -1

