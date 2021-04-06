
DYDX = ((1,0), (-1,0), (0,1), (0,-1))
def trace_word_path(word, grid):
    def trace(word, coords):
        nonlocal result
        if word:
            for y, x in coords:
                if word[0] == grid[y][x] and (y, x) not in path:
                    path.append((y, x))
                    trace(word[1:], [(y+dy, x+dx) for dy,dx in DYDX if \
                                     0<=x+dx<w and 0<=y+dy<h])
                    path.pop()
        else:
            result = path[:]
    
    w, h = len(grid[0]), len(grid)
    path = []
    result = 'Not present'
    trace(word, [(y, x) for x in range(w) for y in range(h)])
    return result

