
def simulate_grass(g, x, y):
    g = [list(i) for i in g]
    stack = [[x, y]]
    
    while stack:
        x, y = stack.pop()
        if g[x][y] != 'o':
            continue
        g[x][y] = '+'
        stack += [[x, y-1], [x-1, y], [x+1, y], [x, y+1]]
        
    return [''.join(i) for i in g]

