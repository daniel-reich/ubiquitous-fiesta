
def playback_duration(duration, speed):
    d = list(map(int,duration.split(':')))
    
    t = d[2] + 60*d[1] + 3600*d[0]
    t = t / speed
    
    d[0] = int(t // 3600)
    t = t - d[0] * 3600
    d[1] = int(t // 60)
    t = t- d[1] * 60
    d[2] = int(t)
    
    myans = str(d[0]).zfill(2) + ':' + str(d[1]).zfill(2) + ':' + str(d[2]).zfill(2)
    
    return myans

