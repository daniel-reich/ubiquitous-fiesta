
def largest_island(lst):
    islands, m, n = [], len(lst), len(lst[0])
    for i in range(m):
        for j in range(n):
            if lst[i][j] == 1:
                if not islands:
                    islands.append([[i, j]])
                else:
                    touch_an_island = False
                    for island in islands:
                        touch = False
                        for dot in island:
                            if abs(dot[0] - i) < 2 and abs(dot[1] - j) < 2:
                                touch = True
                                break
                        if touch:
                            island.append([i, j])
                            touch_an_island = True
                            break
                    if not touch_an_island:
                        islands.append([[i, j]])
    return max(len(island) for island in islands)

