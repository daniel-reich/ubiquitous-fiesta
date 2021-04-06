
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
def all_explode(grid):
    chain = [[(0, 0)]]
    n_total_bombs = sum(c in '+x' for row in grid for c in row)
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
                if not already_in:
                    new_link.append(new_tpl)
                    n_activated_bombs += 1
        if new_link:
            chain.append(new_link)
            activate = True
    return n_total_bombs == n_activated_bombs

