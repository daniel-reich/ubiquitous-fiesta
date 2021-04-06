
def track_robot(*steps):
    lt = [0, 0]
    for i in range(len(steps)):
        if i%2:
            lt[0] += steps[i]*((-1)**(len(steps[1:i+1:2])+1))
        else:
            lt[1] += steps[i]*((-1)**(len(steps[0:i+1:2])+1))
    return lt

