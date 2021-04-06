
def exit_maze(maze, directions):
  for i in range(len(maze)):
    if maze[i].count(2)==1:
      pos1=i
      pos2=maze[i].index(2)
  for dir in directions:
    if(dir=="N"):
      if pos1==0: return "Dead"
      pos1=pos1-1
    if(dir=="S"):
      if pos1==len(maze)-1: return "Dead"
      pos1=pos1+1
    if(dir=="E"):
      if pos2==len(maze[0])-1: return "Dead"
      pos2=pos2+1
    if(dir=="W"):
      if pos2==0: return "Dead"
      pos2=pos2-1
    if(maze[pos1][pos2]==1):return "Dead"
    if(maze[pos1][pos2]==3):return "Finish"
  return "Lost"

