
def exit_maze(maze, directions):
    zeros = set()
    for r, row in enumerate(maze):
        for c, v in enumerate(row):
            if v == 0:
                zeros.add((r, c))
            elif v == 2:
                pos = (r, c)
                zeros.add((r, c))
            elif v == 3:
                finish = (r, c)
    for c in directions:
        if c == "N":
            pos = (pos[0] - 1, pos[1])
        elif c == "S":
            pos = (pos[0] + 1, pos[1])
        elif c == "E":
            pos = (pos[0], pos[1] + 1)
        elif c == "W":
            pos = (pos[0], pos[1] - 1)
        if pos == finish:
            return "Finish"
        elif pos not in zeros:
            return "Dead"
    return "Lost"

