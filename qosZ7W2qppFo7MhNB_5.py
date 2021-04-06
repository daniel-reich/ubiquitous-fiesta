
def hex_distance(grid):
    w = len(grid[0])
    a = ''.join(grid).index('x')
    b = ''.join(grid).index('x', a+1)
    dx, dy = abs(a%w - b%w), abs(a//w - b//w)
    return dy + max(0, (dx-dy) // 2)

