
shifts = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1))
​
​
def is_inside(r, c, rows, cols):
    if 0 <= r < rows and 0 <= c < cols:
        return True
    return False
​
​
def dfs(r, c, rows, cols, visited, area):
    count = [0]
    visited[r][c] = True
    area[0] += 1
    for sh in shifts:
        new_r, new_c = r + sh[0], c + sh[1]
        if is_inside(new_r, new_c, rows, cols) and not visited[new_r][new_c]:
            dfs(new_r, new_c, rows, cols, visited, area)
​
​
def largest_island(matrix) -> int:
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for c in range(cols)] for r in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                visited[r][c] = True
    max_area = 0
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                area = [0]
                dfs(r, c, rows, cols, visited, area)
                max_area = max(area[0], max_area)
​
    return max_area

