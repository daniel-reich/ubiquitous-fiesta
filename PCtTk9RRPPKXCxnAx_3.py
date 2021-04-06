
modulo = lambda x, y: x if abs(x) < abs(y) else modulo([x-y, x+y][x*y < 0], y)

