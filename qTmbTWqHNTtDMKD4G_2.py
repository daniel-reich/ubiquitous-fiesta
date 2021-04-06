
from queue import Queue
def get_path_length(world, width, height):
​
    p2idx = lambda x, y: x * height + y
    p_in_range = lambda x, y: 0 <= x < height and 0 <= y < width
    dirs = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
​
    world = world.split(',')
    q, mrk, op = Queue(), [0] * (width * height), world.index('m')
    ox, oy = op // width, op % width
​
    q.put(((ox, oy), 0))
    mrk[p2idx(ox, oy)] = 1
    while not q.empty():
        p, l = q.get()
        cx, cy = p
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if p_in_range(nx, ny) and not mrk[p2idx(nx, ny)] and world[p2idx(nx, ny)] != 't':
                if world[p2idx(nx, ny)] == 'h': return l + 1
                q.put(((nx, ny), l + 1))
                mrk[p2idx(nx, ny)] = 1
    return -1

