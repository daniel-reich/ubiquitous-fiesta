
def most_overlapped_block(grid_width, points):
    return max(sum(abs(p[0] - x) + abs(p[1] - y) <= p[2] for p in points)
               for x in range(1, grid_width + 1)
               for y in range(1, grid_width + 1))

