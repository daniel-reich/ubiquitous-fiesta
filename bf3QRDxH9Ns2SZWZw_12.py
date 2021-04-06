
def all_explode(grid):
    bombs = [(i,j) for i,x in enumerate(grid) for j, y in enumerate(x) if y in '+x']
    moves,movesd = [(0,1),(1,0),(-1,0),(0,-1)], [(-1,-1),(1,1),(-1,1),(1,-1)]
    stack, visited = [(0,0)], [(0,0)]
​
    while stack:
        i,j = stack.pop()
        move = moves if grid[i][j] == '+' else movesd
        neighbors = [(i+a,j+b)for a, b in move if 0 <= i+a < len(grid) and 0<=j+b <len(grid[0])]
​
        for m,n in neighbors:
            if (m,n) not in visited and grid[m][n] in '+x':
                visited.append((m,n))
                stack.append((m,n))
    return len(bombs) == len(visited)

