
def track_robot(ins):
    coord = [0,0]
    for move in ins:
        moves = move.split()
        if moves[0] == 'right':
            coord[0] += int(moves[1])
        elif moves[0] == 'left':
            coord[0] -= int(moves[1])
        elif moves[0] == 'up':
            coord[1] += int(moves[1])
        elif moves[0] == 'down':
            coord[1] -= int(moves[1])
    
                
    return coord

