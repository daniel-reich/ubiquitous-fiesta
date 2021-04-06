
def get_path_length(world,w,h):
    '''
    Returns the shortest route from Matt's position to his home avoiding trees
    as per the instructions.
    '''
​
    def get_locs(world,i,j):
        '''
        Returns a list of the locations in world which can be reached in 1 step
        from world[i][j]
        '''
        locs = ((i,j-1),(i,j+1),(i-1,j-1),(i-1,j),
                (i-1,j+1),(i+1,j-1),(i+1,j),(i+1,j+1))
​
        return [(a,b) for a,b in locs if 0<=a<h and 0<=b<w and world[a][b] != 't']
    
    world = world.replace(',','')
    matt, home = world.index('m'), world.index('h')
    matt = (matt//w, matt%w)
    home = (home//w, home%w)  # positions in 2d representation of world
    world = [world[i*w:i*w+w] for i in range(h)]
    
    prev =[[None for loc in row] for row in world] # track Matt's route home
    visited = set()
    q = []
    q.append(matt)  # start from where he is
​
    while q:
        i,j = q.pop(0)
        visited.add((i,j))
        if (i,j) == home:   # made it: shouldn't be driving if he's been drinking though!
            current = prev[home[0]][home[1]]
            count = 0
            while current:
                count += 1
                current = prev[current[0]][current[1]]
​
            return count
​
        for a,b in get_locs(world,i,j):
            if (a,b) not in visited and (a,b) not in q:
                prev[a][b] = (i,j)  # their predecessor
                q.append((a,b))
​
    return -1  # he's trapped by trees!

