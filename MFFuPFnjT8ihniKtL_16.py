
def bug_jump(height, time):
    a=height**0.5*-2
    time=time/1000
    if(pos(time,a)<0):
        return[0,None]
    if(len(str(pos(time,a)))>9):
        return[round(pos(time,a),2),gradient(time,a)]
    return[pos(time,a),gradient(time,a)]
def gradient(x,a):
    if(x>-a):
        return None
    g= -2*x-a
    if(g==0):
        return None
    elif(g>0):
        return "up"
    else:
        return "down"
def pos(x,a):
    return -x**2-a*x

