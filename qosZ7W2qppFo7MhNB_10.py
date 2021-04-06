
def hex_tiles(tiles,loc):
    '''
    Returns the addresses of the tiles which are adjacent to the tile at loc.
    '''
    i, j = loc
    possibles = ((i-1,j-1),(i-1,j+1),(i,j-2),
                 (i,j+2),(i+1,j-1),(i+1,j+1))
    return [(a,b) for a, b in possibles if 0 <= a < len(tiles) and \
            0 <= b < len(tiles[0]) and tiles[a][b] != ' ']
​
def count_steps(start, end, tiles):
    '''
    Returns the minimum number of steps between tile start and tile end
    '''
    q = [start]
    visited = set()
    prev = [[-1 for j in range(len(tiles[0]))] for i in range(len(tiles))]
​
    while q:
        tile = q.pop(0)
        if tile == end:
            break
        visited.add(tile)
        for i, j in hex_tiles(tiles, tile):
            if (i,j) not in visited and (i,j) not in q:
                prev[i][j] = (tile[0],tile[1])
                q.append((i,j))
​
    count = 0
    next_tile = end
    while next_tile != start:
        count += 1
        next_tile = prev[next_tile[0]][next_tile[1]]
​
    return count
​
def hex_distance(tiles):
    '''
    Returns the shortest distance between the 2 tiles in tiles marked 'x' as
    per instructions.
    '''
    x1, x2 = [(i,j) for i in range(len(tiles)) for j in range(len(tiles[0])) \
              if tiles[i][j] == 'x']
    return count_steps(x1, x2, tiles)

