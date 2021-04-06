
def exit_maze(maze, directions):
    for i in maze:
        if 2 in i:
            position = [maze.index(i), i.index(2)]
    for i in directions:
        if i == "N":
            if position[0] == 0:
                return "Dead" 
            else:
                position[0] = position[0] - 1
        elif i == "S":
            if position[0] == 9:
                return "Dead"
            else:
                position[0] = position[0] + 1
        elif i == "E":
            if position[1] == 9:
                return 'Dead'
            else:
                position[1] = position[1] + 1
        else:
            if position[1] == 0:
                return 'Dead'
            else:
                position[1] = position[1] - 1
        if maze[position[0]][position[1]] == 1:
            return 'Dead'
        if maze[position[0]][position[1]] == 3:
            return "Finish"
    return "Lost"

