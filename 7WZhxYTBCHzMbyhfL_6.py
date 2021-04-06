
def knight_moves(i, j):
    '''
    Returns a list of coordinates of the moves a knight can make from this
    location. Coordinates 1 to 8 in each dimension.
    '''
    possibles = ((2,1),(1,2),(-1,2),(-2,1),
                 (-2,-1),(-1,-2),(1,-2),(2,-1))
​
    return [(r+i,c+j) for r, c in possibles if 1 <= r+i <= 8 and 1 <= c+j <= 8]
​
GRAPH = {(i,j): knight_moves(i, j) for i in range(1,9) for j in range(1,9)}
#print(GRAPH)
​
def knight_bfs(start_i, start_j, end_i, end_j):
    '''
    Returns the minimum number of moves needed to legitimately move a knight
    from start to end as per instructions.
    '''
    visited = set()
    q = [(start_i, start_j)]
    prev = {square: -1 for square in GRAPH}  # to store path.
    
    while q:
        r, c = q.pop(0)
        if (r, c) == (end_i, end_j):  # reached target square
            count = 0
            square = (end_i, end_j)
            
            while prev[square] != -1:
                count += 1
                square = prev[square]
​
            return count
​
        visited.add((r, c))
        for k, l in GRAPH[(r, c)]:
            if (k, l) not in visited:
                prev[(k, l)] = (r, c)
                q.append((k, l))   # queue bfs order
​
    raise ValueError   # no path found - error!!

