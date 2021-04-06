
def all_explode(grid):
  if grid[0][0]=='+':
    grid = tbomb(grid,0,0)
  elif grid[0][0]=='x':
    grid = xbomb(grid,0,0)
  return all([all([j=='0' for j in i]) for i in grid])
  
def tbomb(lst,y,x):
  lst[y][x] = '0'
  if y>0:
    if lst[y-1][x]=='+':
      lst = tbomb(lst,y-1,x)
    elif lst[y-1][x]=='x':
      lst = xbomb(lst,y-1,x)
  if y<len(lst)-1:
    if lst[y+1][x]=='+':
      lst = tbomb(lst,y+1,x)
    elif lst[y+1][x]=='x':
      lst = xbomb(lst,y+1,x)
  if x>0:
    if lst[y][x-1]=='+':
      lst = tbomb(lst,y,x-1)
    elif lst[y][x-1]=='x':
      lst = xbomb(lst,y,x-1)
  if x<len(lst[0])-1:
    if lst[y][x+1]=='+':
      lst = tbomb(lst,y,x+1)
    elif lst[y][x+1]=='x':
      lst = xbomb(lst,y,x+1)
  return lst
  
def xbomb(lst,y,x):
  lst[y][x] = '0'
  if y>0:
    if x>0:
      if lst[y-1][x-1]=='+':
        lst = tbomb(lst,y-1,x-1)
      elif lst[y-1][x-1]=='x':
        lst = xbomb(lst,y-1,x-1)
    if x<len(lst[0])-1:
      if lst[y-1][x+1]=='+':
        lst = tbomb(lst,y-1,x+1)
      elif lst[y-1][x+1]=='x':
        lst = xbomb(lst,y-1,x+1)
  if y<len(lst)-1:
    if x>0:
      if lst[y+1][x-1]=='+':
        lst = tbomb(lst,y+1,x-1)
      elif lst[y+1][x-1]=='x':
        lst = xbomb(lst,y+1,x-1)
    if x<len(lst[0])-1:
      if lst[y+1][x+1]=='+':
        lst = tbomb(lst,y+1,x+1)
      elif lst[y+1][x+1]=='x':
        lst = xbomb(lst,y+1,x+1)
  return lst

