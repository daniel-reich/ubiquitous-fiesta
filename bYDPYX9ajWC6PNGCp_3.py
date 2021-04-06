
def track_robot(*steps, facing = 0):
    pos = [0,0]
    for i in range(len(steps)):
        facing %= 4
        if facing == 0:
            pos[1] += steps[i]
        elif facing == 1:
            pos[0] += steps[i]
        elif facing == 2:
            pos[1] -= steps[i]
        elif facing == 3:
            pos[0] -= steps[i]
        facing +=1
            
    return list(pos)

