
def exit_maze(maze, directions):
  try:
    for x in range(len(maze)):
      if 2 in maze[x]:
        y = [x, maze[x].index(2)]
        for z in directions:
          if z == "N":
            w = maze[y[0]-1][y[-1]]
            if w == 1:
              return "Dead"
            elif w == 3:
              return "Finish"
            else:
              y = [y[0]-1, y[-1]]
          if z == "S":
            w = maze[y[0] + 1][y[-1]]
            if w == 1:
              return "Dead"
            elif w == 3:
              return "Finish"
            else:
              y = [y[0] + 1, y[-1]]
          if z == "E":
            w = maze[y[0]][y[-1] + 1]
            if w == 1:
              return "Dead"
            elif w == 3:
              return "Finish"
            else:
              y = [y[0], y[-1] + 1]
          if z == "W":
            w = maze[y[0]][y[-1] - 1]
            if w == 1:
              return "Dead"
            elif w == 3:
              return "Finish"
            else:
              y = [y[0], y[-1] - 1]
        return "Lost"
  except IndexError:
    return "Dead"

