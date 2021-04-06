
def dfs(word, s, grid, H, W, row, col, chain):
    if len(chain) == len(word):
        return chain
    for [row2, col2] in [[row - 1, col], [row + 1, col], [row, col + 1], [row, col - 1]]:
        if 0 <= row2 < H and 0 <= col2 < W and grid[row2][col2] == s[0] and \
           (row2, col2) not in chain:
            new_chain = chain[:]
            new_chain.append((row2, col2))
            if len(new_chain) == len(word):
                return new_chain
            chain2 = dfs(word, s[1:], grid, H, W, row2, col2, new_chain)
            if len(chain2) == len(word):
                return chain2
    return chain
​
def trace_word_path(word, grid):
    H, W = len(grid), len(grid[0])
    for row in range(H):
        for col in range(W):
            if grid[row][col] == word[0]:
                chain = dfs(word, word[1:], grid, H, W, row, col, [(row, col)])
                if len(chain) == len(word):
                    return chain
    return 'Not present'

