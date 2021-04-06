
def find_neighbors(g, r, c):
    n_rows, n_cols = len(g), len(g[0])
    if g[r][c] == '+':
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    elif g[r][c] == 'x':
        neighbors = [(-1, -1), (1, 1), (1, -1), (-1, 1)]
    return [(r + tpl[0], c + tpl[1]) for tpl in neighbors
            if 0 <= r + tpl[0] < n_rows and
            0 <= c + tpl[1] < n_cols and
            g[r + tpl[0]][c + tpl[1]] in '+x']
​
​
def make_chain(grid, row, col):
    chain = [[(row, col)]]
    activate = True
    n_activated_bombs = 1
    while activate:
        activate = False
        previous_link = chain[-1]
        new_link = []
        for p_tpl in previous_link:
            for new_tpl in find_neighbors(grid, *p_tpl):
                already_in = False
                for lst in chain:
                    if new_tpl in lst:
                        already_in = True
                        break
                if not already_in and new_tpl not in new_link:
                    new_link.append(new_tpl)
                    n_activated_bombs += 1
        if new_link:
            chain.append(new_link)
            activate = True
    return {tpl for link in chain for tpl in link}
​
​
def min_bombs_needed(grid):
    remaining_bombs = {(r, c) for r, row in enumerate(grid)
                       for c, val in enumerate(row) if val in '+x'}
    chain_count = 0
    while remaining_bombs:
        chain = make_chain(grid, *remaining_bombs.pop())
        remaining_bombs -= chain
        chain_count += 1
    return chain_count

