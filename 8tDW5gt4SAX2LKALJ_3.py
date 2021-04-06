
from itertools import combinations
def min_bombs_needed(grid):
  bombs = []
  grid = tuple([tuple(i) for i in grid])
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      if grid[y][x] in '+x':
        bombs.append([y,x])
  for l in range(1,len(bombs)+1):
    for c in combinations(bombs,l):
      if explode([list(i) for i in grid],c):
        return l
    
def explode(lst,bombs):
  for i in bombs:
    y,x = i
    if lst[y][x]=='+':
      lst = tbomb(lst,y,x)
    elif lst[y][x]=='x':
      lst = xbomb(lst,y,x)
  return all([all([i=='0' for i in j]) for j in lst])
​
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
  if x<len(lst[y])-1:
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
    if x<len(lst[y])-1:
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
    if x<len(lst[y])-1:
      if lst[y+1][x+1]=='+':
        lst = tbomb(lst,y+1,x+1)
      elif lst[y+1][x+1]=='x':
        lst = xbomb(lst,y+1,x+1)  
  return lst

