
def bug_jump(y_max, t):
    time = t/1000
    t_top = y_max**(1/2)
    t_max = 2 * t_top 
    y = -(time)**2 + t_max * time   
    if(time < t_top):
        direction = "up"
    elif (time < 2*t_top):
        direction = "down"
    else:
        y = 0
        direction = None
    return [round(y, 2), direction]

