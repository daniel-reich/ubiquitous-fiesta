
directions = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
rev_directions = {value: key for key, value in directions.items()}
​
def final_direction(initial, turns):
    direction = directions[initial]
    for turn in turns:
        if turn == 'R':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
    return rev_directions[direction]

