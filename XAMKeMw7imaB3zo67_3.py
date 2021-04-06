
def trace_word_path(word, grid):
    rows, cols, len_word = len(grid), len(grid[0]), len(word)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == word[0]:
                idx_chain = [(r, c)]
                for idx_w in range(1, len_word):
                    row, col = idx_chain[-1]
                    letter_found = False
                    for tpl in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        candidate = (row + tpl[0], col + tpl[1])
                        if (0 <= candidate[0] < rows and
                            0 <= candidate[1] < cols and
                            candidate not in idx_chain and
                            grid[candidate[0]][candidate[1]] == word[idx_w]):
                            idx_chain.append(candidate)
                            letter_found = True
                            break
                    if not letter_found:
                        break
                if len(idx_chain) == len_word:
                    return idx_chain
    return 'Not present'

