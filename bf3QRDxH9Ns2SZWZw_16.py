
from collections import deque
​
​
def explode(idx, bombtype, max_x, max_y):
    x, y = idx
    chain = {'+': [(1, 0), (0, 1), (0, -1), (-1, 0)],
             'x': [(1, 1), (-1, 1), (1, -1), (-1, -1)],
             '0': [(0, 0)]}
    return [(x+i, y+j) for i, j in chain[bombtype]
            if 0 <= x+i <= max_x and 0 <= y+j <= max_y]
​
​
def all_explode(grid):
    max_x, max_y = len(grid[0]) - 1, len(grid) - 1
    queue = deque([(0, 0)])
    avail_bombs = sum(i == '+' or i == 'x' for row in grid for i in row)
    exploded = [(j, i) for i, row in enumerate(grid)
                for j, v in enumerate(row) if v == '0']
    while queue:
        x, y = queue.pop()
        new_explosions = explode((x, y), grid[y][x], max_x, max_y)
        for explosion in new_explosions:
            if explosion not in exploded:
                avail_bombs -= 1
                if not avail_bombs:
                    return True
                exploded.append(explosion)
                queue.appendleft(explosion)
    return False

