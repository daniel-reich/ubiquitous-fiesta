
def all_explode(grid):
  pos = {(i,j) for i in range(len(grid)) for j in range(len(grid[0]))}
  bombs = {(i,j) for (i,j) in pos if grid[i][j] in 'x+'}
  
  queue = [(0,0)]
  exploded = set()
  while queue:
    (x,y) = queue.pop(0)
    if grid[x][y] == "+":
      dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    else:
      dirs = [(1,1),(-1,1),(1,-1),(-1,-1)]
    for (i,j) in dirs:
      if (x+i,y+j) in bombs and (x+i,y+j) not in exploded:
        exploded = exploded.union({(x+i,y+j)})
        queue+= [(x+i,y+j)]
  
  return exploded == bombs

