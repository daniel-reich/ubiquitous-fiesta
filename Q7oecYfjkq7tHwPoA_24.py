
def climb(stamina, obstacles,count=0):
    if len(obstacles) == 1 and stamina > 0:
        return count
    elif stamina < 0:
        return count-1
    elif stamina == 0:
        return count
    #False for climbing down, True for climbing up
    updown = {False:1,True:2}
    diff = obstacles[1] - obstacles[0]
    key = bool(diff + abs(diff))
    ones = abs(diff) // 1
    rem = round(abs(diff) % 1, 1)
    loss = (ones + bool(rem))*updown[key]
    stamina -= loss
    return climb(stamina, obstacles[1:],count+1)

