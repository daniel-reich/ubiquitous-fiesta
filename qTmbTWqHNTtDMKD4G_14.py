
from itertools import chain
​
def get_path_length(world, w, h):
    def go_to(pos):
        x, y = pos%w, pos//w
        for dx, dy in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
            if 0<=x+dx<w and 0<=y+dy<h:
                yield x+dx + w*(y+dy)
    
    world = world.split(',')
    res = 0
    todo = [world.index('m')]
    while todo:
        res += 1
        new_todo = []
        for i in chain(*map(go_to, todo)):
            if world[i] == 'h': return res
            elif world[i] == '.':
                world[i] = '*'
                new_todo.append(i)
        todo = new_todo
    return -1

