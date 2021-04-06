
def exit_maze(_, directions, x=9, y=8):
    if x > 9 or y > 9 or x < 0 or y < 0 or maze[x][y] == 1:
        return "Dead"
    if maze[x][y] == 3:
        return "Finish"
    if not directions:
        return "Lost"
    else:
        direction = directions[0]
        if direction == "N":
            return exit_maze(_, directions[1:], x - 1, y)
        if direction == "S":
            return exit_maze(_, directions[1:], x + 1, y)
        if direction == "E":
            return exit_maze(_, directions[1:], x, y + 1)
        if direction == "W":
            return exit_maze(_, directions[1:], x, y - 1)

