
 def get_path_length(world, width, height):
    world = world.split(',')
    mat =  [world[idx:(idx+width)] for idx in range(0,height*width-1, height)]
    start = world.index('m')//width, world.index('m')%width
    goal = world.index('h')//width, world.index('h')%width
    current_level, visited = {start}, set()
​
    def neighbors(y,x):
        def can_go(y_,x_):
            return 0<=y_<height and 0<=x_<width and mat[y_][x_]!='t'
        directions = [(-1,-1),(-1, 0),(-1, 1),( 0,-1),
                      ( 0, 1),( 1,-1),( 1, 0),( 1, 1),]
        return [(y+dy, x+dx) for dy, dx in directions if can_go(y+dy, x+dx)]
​
    depth = 0
    while current_level:
        if goal in current_level:
            return depth
        current_level = {n for pos in current_level for n in neighbors(*pos)} - visited
        visited.update(current_level)
        depth += 1
    return -1

