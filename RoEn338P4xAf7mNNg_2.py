
def bfs(grid, start, stop):
    queue = [start]
    visited = {start:None}
    moves = [(0,1),(1,0),(-1,0),(0,-1)]
    while queue:
        m, n = queue.pop(0)
        if grid[m][n] == stop:
            return visited, (m,n)
        neighbors = [(m+a, n+b) for a, b in moves if 0 <= m+a < len(grid) and 0 <= n+b < len(grid[0])]
        for neighbor in neighbors:
            if neighbor not in visited:
                visited[neighbor] = (m,n)
                queue.append(neighbor)
    return visited, None
def shortest_path(lst):
    total = 0
    for i,x in enumerate(lst):
        for j,y in enumerate(x):
            if y == '1':
                start = (i,j)
                num = y
                while True:
                    visited, stop_index = bfs(lst, start, str(int(num)+1))
                    if not stop_index:
                        break
                    count = 0
                    start = stop_index
                    current = stop_index
                    while visited.get(current):
                        count += 1
                        current = visited.get(current)
                    num = str(int(num)+1)
                    total += count
                    
                break
    return total

