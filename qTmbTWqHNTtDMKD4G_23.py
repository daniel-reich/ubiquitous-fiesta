
def get_path_length(world, width, height):
    world = world.split(',')
    grid = [world[k*width:k*width+width] for k in range(height)]
    for r in range(height):
        for c in range(width):
            if grid[r][c] == 'm':
                rmatt, cmatt = r, c
            elif grid[r][c] == 'h':
                rhome, chome = r, c
    queue = [(rmatt, cmatt)]
    distance = {(rmatt, cmatt): 0}
    while len(queue) > 0:
        row, col = queue.pop(0)
        for rdiff, cdiff in [[1, 0], [-1, 0], [0, 1], [0, -1],
                             [1, 1], [1, -1], [-1, 1], [-1, -1]]:
            row2, col2 = row + rdiff, col + cdiff
            if 0 <= row2 < height and 0 <= col2 < width and \
               grid[row2][col2] != 't' and (row2, col2) not in distance:
                queue.append((row2, col2))
                distance[(row2, col2)] = distance[(row, col)] + 1
                if (row2, col2) == (rhome, chome):
                    return distance[(row2, col2)]
    return -1

