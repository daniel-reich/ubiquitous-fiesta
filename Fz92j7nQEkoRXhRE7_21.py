
def jumping_frog_recursive(
        stones,
        frog_position,
        previous_positions):
​
    def get_new_position_options(stones, frog_position):
        if frog_position < 0:
            return[0]
        else:
            j = stones[frog_position]
            if j == 0:
                return []
            new_position_options = []
            if j <= frog_position:
                new_position_options.append(frog_position - j)
            new_position_options.append(frog_position + j)
            return new_position_options
    
    if frog_position >= len(stones):
        return len(previous_positions)
    elif frog_position in previous_positions:
        return None
    else:
        new_position_options = get_new_position_options(stones, frog_position)
        shortest_path = None
        for new_frog_position in new_position_options:
            path = jumping_frog_recursive(
                stones,
                new_frog_position,
                previous_positions + [frog_position])
            if shortest_path is None or (path is not None and path < shortest_path):
                shortest_path = path
        return shortest_path
​
def jumping_frog(n, stones):
    return jumping_frog_recursive(stones, -1, []) or "no chance :-("

