
from itertools import product
        
def knight_bfs(a, b, c, d, depth=0, deltas=[-2, -1, 1, 2]):
    visited = {(a, b), }
    while (c, d) not in visited:
        visited.update({(x +dx, y +dy) for (x, y), dx, dy  \
            in product(visited, deltas, deltas) if \
            (dx+dy)%2 and 1 <= x +dx <= 8 and 1 <= y +dy <= 8})
        depth += 1
    return depth

