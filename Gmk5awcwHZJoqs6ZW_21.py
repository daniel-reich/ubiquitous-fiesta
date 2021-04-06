
def largest_island(lst):
    offsets = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
    rows, cols = len(lst), len(lst[0])
    all_islands = []
    
    while any(1 in x for x in lst):
        for i in range(rows):
            for j in range(cols):
                if lst[i][j] == 1:
                    visited = set()
                    stack = [(i, j)]
                    while stack:
                        i, j = stack.pop()
                        if (i, j) not in visited and lst[i][j] == 1:
                            visited.add((i, j))
                            for r, c in offsets:
                                if 0 <= i+r < rows and 0 <= j+c < cols: 
                                    stack.append((i+r, j+c))
                    all_islands.append(len(visited))
                    for i, j in visited:
                        lst[i][j] = 0
            
    return sorted(all_islands)[-1]

