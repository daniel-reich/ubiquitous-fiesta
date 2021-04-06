
def get_path_length(world, width, height):
    lst_w = world.split(',')
    lst_2d = []
    for r in range(height):
        lst_2d.append(lst_w[:width])
        lst_w = lst_w[width:]
    all_dots = set()
    for r in range(height):
        for c in range(width):
            if lst_2d[r][c] == '.':
                all_dots.add((r, c))
            elif lst_2d[r][c] == 'm':
                start = (r, c)
            elif lst_2d[r][c] == 'h':
                finish = (r, c)
    steps = 0
    link = [start]
    while link:
        new_link = []
        steps += 1
        for pos in link:
            for move in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1),
                         (0, -1), (-1, -1)]:
                new_pos = (pos[0] + move[0], pos[1] + move[1])
                if new_pos == finish:
                    return steps
                elif new_pos in all_dots:
                    new_link.append(new_pos)
                    all_dots -= {new_pos}
        link = new_link
    return -1

