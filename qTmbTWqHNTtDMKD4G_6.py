
def get_path_length(world, c, r):
  world = world.replace(",","")
  s,f = world.index("m"), world.index("h")
  world = [[world[c*i+j] for j in range(c)] for i in range(r)]
  s, f = (s//c, s%c), (f//c, f%c)
  dirs = {(1,1),(1,0),(0,1),(-1,-1),(-1,0),(0,-1),(1,-1),(-1,1)}
  mapp = {(i,j):world[i][j] for j in range(c) for i in range(r)}
  
  dis = {s:0}
  queue = [s]
  while queue:
    i,j = queue.pop(0)
    for (k,l) in dirs:
      if (i+k,j+l) in mapp and mapp[(i+k,j+l)]!="t" and (i+k,j+l) not in dis:
        dis[(i+k,j+l)] = dis[(i,j)]+1
        queue+= [(i+k,j+l)]
  
  return dis[f] if f in dis else -1

