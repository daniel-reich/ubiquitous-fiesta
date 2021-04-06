
def diamond(carat):
  
  grid = []
  
  if carat % 2 == 1:
    for i in range(carat):
      grid.append([])
  else:
    for i in range(carat-1):
      grid.append([])
    
    
  for row in grid:
    for i in range(carat):
      row.append(0)
      
  mid = len(grid) // 2
  top_half = True
  
  if carat % 2 == 1:
    indices = [mid-1,mid+1]
  else:
    indices = [mid-1,mid+2]
    
  for i in range(len(grid)):
    
    if i == 0 or i == len(grid) - 1:
      grid[i][mid] = 1
      if carat % 2 == 0:
        grid[i][mid+1] = 1
    
    else:
      grid[i][indices[0]] = 1
      grid[i][indices[1]] = 1
      
      if i >= mid:
        top_half = False
        
      if top_half:
        indices[0] -= 1
        indices[1] += 1
        
      else:
        indices[0] += 1
        indices[1] -= 1
  if carat % 2 == 1:
    return [grid, 'perfect cut']
  else:
    return [grid, 'good cut']

