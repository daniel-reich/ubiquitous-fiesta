
def all_explode(bomb_grid):
    '''
    bomb_grid is a 2d grid of bombs and empty spaces as explained in the
    instructions. Returns True if exploding a bomb in top left corner causes
    all bombs in the grid to explode too.
    '''
    def bomb_neighbours(grid, i, j):
        '''
        Returns the neighbours of bomb grid[i][j] which will explode based
        on its bomb type if it is a bomb and explodes.
        '''
        bomb = grid[i][j]
        if bomb == '0':
            return []  # not a bomb
        
        all_neighbours = [(grid[r][c],r,c) for r in range(max(0,i-1),min(len(grid),i+2))\
                          for c in range(max(0,j-1),min(len(grid[0]),j+2)) if grid[r][c] != '0' \
                          and not(i==r and j==c)]
        
        if bomb == '+':
            return [(a,b,c) for a,b,c in all_neighbours if b==i and c==j-1 or b==i and c==j+1 \
                    or b==i-1 and j==c or b==i+1 and j==c]  # bomb neighbours of '+' bomb
        return [(a,b,c) for a,b,c in all_neighbours if b==i-1 and c==j-1 or b==i-1 and c==j+1\
                    or b==i+1 and c==j-1 or b==i+1 and c==j+1] # bomb neighbours of 'x' bomb
​
    exploded = set()  # stores grid addresses of exploded bombs
    q = []
    q.append((bomb_grid[0][0],0,0))
​
    while q:
        bomb, i, j = q.pop(0)   # get nearest bomb and its position
        exploded.add((i,j))
        
        for bomb2, r, c in bomb_neighbours(bomb_grid, i, j):
            if (r,c) not in exploded:
                q.append((bomb_grid[r][c],r,c))
​
    return len(exploded) == sum(1 for i in range(len(bomb_grid)) for j in range(len(bomb_grid[0]))\
                                if bomb_grid[i][j] != '0')

