
def exit_maze(maze, directions):
  pos=[0,0]
  for i in range(len(maze)):
    for j in range(len(maze[i])):
      if maze[i][j]==2:
        pos[0]+=i
        pos[1]+=j
        for k in directions:
          if k=='N': pos[0]-=1
          if k=='E': pos[1]+=1
          if k=='S': pos[0]+=1
          if k=='W': pos[1]-=1
          if pos[0]<0 or pos[0]>9 or pos[1]<0 or pos[1]>9 or maze[pos[0]][pos[1]]==1:
            return 'Dead'
          if maze[pos[0]][pos[1]]==3:return 'Finish'
        return 'Lost'

