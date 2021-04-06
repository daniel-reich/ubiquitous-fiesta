
def min_bombs_needed(map):
    num_bombs_set_off = 0
    def in_bounds(coords):
        return coords[0] >= 0 and coords[0] < len(map) and coords[1] >= 0 and coords[1] < len(map[0])
​
    def explode_bomb(coords):
        if not in_bounds(coords):
            return
​
        bomb_type = map[coords[0]][coords[1]]
        if bomb_type == "0":
            return map
        map[coords[0]][coords[1]] = "0"
​
        if bomb_type == "+":
            explode_bomb([coords[0] + 1, coords[1]])
            explode_bomb([coords[0] - 1, coords[1]])
            explode_bomb([coords[0], coords[1] + 1])
            explode_bomb([coords[0], coords[1] - 1])
​
        else:
            explode_bomb([coords[0] + 1, coords[1] + 1])
            explode_bomb([coords[0] - 1, coords[1] - 1])
            explode_bomb([coords[0] - 1, coords[1] + 1])
            explode_bomb([coords[0] + 1, coords[1] - 1])
​
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] != "0":
                num_bombs_set_off += 1
                explode_bomb([i,j])
    return num_bombs_set_off

