
def min_bombs_needed (bombs_grid):
    '''
    Returns the minimum number of bombs needed to explode all the bombs.
    '''
    def bomb_neighbours(grid, i, j):
        '''
        Returns the neighbours of bomb grid[i][j] which will explode based
        on its bomb type if it is a bomb and explodes.
        '''
        bomb = grid[i][j]
        if bomb == '0':
            return []  # not a bomb
        
        all_neighbours = [(r,c) for r in range(max(0,i-1),min(len(grid),i+2))\
                          for c in range(max(0,j-1),min(len(grid[0]),j+2)) if grid[r][c] != '0' \
                          and not(i==r and j==c)]
        
        if bomb == '+':
            return [(b,c) for b,c in all_neighbours if b==i and c==j-1 or b==i and c==j+1 \
                    or b==i-1 and j==c or b==i+1 and j==c]  # bomb neighbours of '+' bomb
        return [(b,c) for b,c in all_neighbours if b==i-1 and c==j-1 or b==i-1 and c==j+1\
                    or b==i+1 and c==j-1 or b==i+1 and c==j+1] # bomb neighbours of 'x' bomb
​
    def exploded_bombs(grid, i, j, exploded):
        '''
        Updates exploded with any bombs not already exploded as a result of the bomb
        at grid[i][j] exploding.
        '''
        q = []
        q.append((i,j))
​
        while q:
            i, j = q.pop(0)   # get nearest bomb and its position
            exploded.add((i,j))
        
            for r, c in bomb_neighbours(grid, i, j):
                if (r,c) not in exploded:
                    q.append((r,c))
        
    exploded = set()
    count = 0
    
    for i in range(len(bombs_grid)):
        for j in range(len(bombs_grid[0])):
            if bombs_grid[i][j] != '0' and (i,j) not in exploded:
                exploded_bombs(bombs_grid,i,j,exploded)
                count += 1
​
    return count

