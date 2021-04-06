
def count_word(grid, word):
    count = 0
    sps = [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == word[0]]
    for r, c in sps:
        for dr, dc in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
            lst, y, x = [(r, c)], r, c
            for i in range(1, len(word)):
                y += dr
                x += dc
                if 0<=y<len(grid) and 0<=x<len(grid[0]) and grid[y][x].upper() == word[i]:
                    lst.append((y, x))
                else:
                    break
            if len(lst) == len(word):
                count += 1
                for y, x in lst:
                    grid[y][x] = grid[y][x].lower()
    return (count, grid)

