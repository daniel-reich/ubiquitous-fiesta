
def lines(r, c, rows, cols, n):
    res = []
    if rows - r >= n:
        res.append([(r + i, c) for i in range(n)])
    if r >= n - 1:
        res.append([(r - i, c) for i in range(n)])
    if cols - c >= n:
        res.append([(r, c + i) for i in range(n)])
    if c >= n - 1:
        res.append([(r, c - i) for i in range(n)])
    if rows - r >= n and cols - c >= n:
        res.append([(r + i, c + i) for i in range(n)])
    if r >= n - 1 and c >= n - 1:
        res.append([(r - i, c - i) for i in range(n)])
    if rows - r >= n and c >= n - 1:
        res.append([(r + i, c - i) for i in range(n)])
    if r >= n - 1 and cols - c >= n:
        res.append([(r - i, c + i) for i in range(n)])
    return res
​
​
def count_word(grid, word):
    rows, cols, len_word, count = len(grid), len(grid[0]), len(word), 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c].upper() == word[0]:
                for line in lines(r, c, rows, cols, len_word):
                    tmp_word = ''.join(grid[tpl[0]][tpl[1]].upper()
                                       for tpl in line)
                    if tmp_word == word:
                        count += 1
                        for tpl in line:
                            grid[tpl[0]][tpl[1]] = grid[tpl[0]][tpl[1]].lower()
    return count, grid

