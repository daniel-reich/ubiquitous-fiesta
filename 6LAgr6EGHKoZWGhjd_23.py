
def final_direction(current, moves):
    compass = ["N", "E", "S", "W"]
    current_position = compass.index(current)
    count_moves = 0
    for move in moves:
        if move == "L":
            count_moves -= 1
        if move == "R":
            count_moves += 1
    if count_moves >= 0:
        net_moves = count_moves % 4
    elif count_moves < 0:
        net_moves = abs(count_moves) % 4
        net_moves = net_moves * -1
    gross_position = current_position + net_moves
​
    if gross_position > 3:
        return compass[gross_position - 4]
    if gross_position < 0:
        return compass[(len(compass))-abs(gross_position)]
    else:
        return compass[gross_position]

