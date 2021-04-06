
maze = []
def move(x, y):
  if x <0 or y< 0 or x>=len(maze) or y>=len(maze[0]):return False
  if maze[x][y]==1:return False
  if y == len(maze[0])-1:return True
  
  maze[x][y]=1
  return move(x+1, y) or move(x-1, y) or move(x, y+1) or move(x, y-1)
  
def can_enter_cave(lst):
  global maze
  maze = lst
  for i in range(len(maze)):
    if move(i, 0):return True
  return False

