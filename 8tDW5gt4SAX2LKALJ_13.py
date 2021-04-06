
def min_bombs_needed(grid):
    visited, count = [], 0
    moves, moved = [(0,1),(1,0),(-1,0),(0,-1)], [(-1,-1),(-1,1),(1,1),(1,-1)]
    for i, row in enumerate(grid):
        for j, bomb in enumerate(row):
            if not (i,j) in visited and bomb in 'x+':
                stack = [(i,j)]
                count += 1
                move = moved if bomb == 'x' else moves
                visited.append((i,j))
​
                while stack:
                    x, y = stack.pop()
                    neighbors = [(x+a,y+b) for a, b in move if 0 <= x+a < len(grid) and 0 <= y+b < len(row)]
​
                    for m,n in neighbors:
                        if not (m,n) in visited and grid[m][n] in 'x+':
                            stack.append((m,n))
                            visited.append((m,n))
    return count

