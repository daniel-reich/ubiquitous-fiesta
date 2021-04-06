
def get_path_length(world, width, height):
  coords = lambda i: (i//width, i%width)
  
  wmap = world.replace(',', '')
  matt, home = coords(wmap.index('m')), coords(wmap.index('h'))
  graph = [[None if c != 't' else c for c in wmap[i:i+width]] for i in range(0, width*height, width)]
  
  # lamdas
  dist = lambda c1, c2: max(abs(c1[0]-c2[0]), abs(c1[1]-c2[1]))
  neighbours = lambda r, c: [(r + y, c + x) for x, y in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)] if 0<=r+y<height and 0<=c+x<width and graph[r+y][c+x] != 't']
  
  # A* algorithm
  open, closed = {matt: (0, dist(matt, home), None)}, set() # coords: (g, f, heuristic)
  curr = matt
  while curr != home:
    currnode = open[curr]
    del open[curr]
    closed.add(curr)
    for node in neighbours(*curr):
      if not node in closed:
        r,c = node
        cn = graph[r][c]
        g = 1 + currnode[0]
        f = g + dist(node, home)
        if cn  == None or f < cn[1]:
          graph[r][c] = (g, f, f-g)
        open[node] = graph[r][c]
    if not open: return -1
    next = min(open.items(), key=lambda kv: (kv[1][1], kv[1][2])) # discriminate by f value then dist from home
    curr = next[0]
  return graph[home[0]][home[1]][0]

