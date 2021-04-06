
def neibours(grid, row, column):
    n = 0
    cells = [[-1, 0], [-1, +1], [0, +1], [+1, +1], [+1, 0], [+1, -1], [0, -1], [-1, -1]]
    for c in cells:
        if row+c[0] in range(len(grid)) and column+c[1] in range(len(grid[0])):
            n += grid[row+c[0]][column+c[1]]
    return n
​
​
def nextgen(old):
    new = [l[:] for l in old]
    for r in range(len(new)):
        for c in range(len(new[0])):
            if neibours(old, r, c) == 3:
                new[r][c] = 1
            elif neibours(old, r, c) not in [2, 3]:
                new[r][c] = 0
​
    return new
​
​
def game_of_life(board):
    return '\n'.join(''.join(['_', 'I'][i] for i in l) for l in nextgen(board))

