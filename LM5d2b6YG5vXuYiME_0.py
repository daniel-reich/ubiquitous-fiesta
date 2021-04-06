
def can_enter_cave(lst):
    offsets = ((0, -1), (-1, 0), (0, 1), (1, 0))
    rows, cols = len(lst), len(lst[0])
    
    for start in range(rows):
        visited = set()
        stack = [(start, 0)]
​
        while stack:
            i, j = stack.pop()
            if (i, j) not in visited and lst[i][j] == 0:
                if j == cols - 1:
                    return True
                visited.add((i, j))
                for r, c in offsets:
                    if 0 <= i+r < rows and 0 <= j+c < cols: 
                        stack.append((i+r, j+c))
    return False

