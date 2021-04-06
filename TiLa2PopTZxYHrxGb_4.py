
def playback_duration(duration, speed):
    r = []
    x =(int(duration.split(':')[0])*60*60 + int(duration.split(':')[1])*60+int(duration.split(':')[2]))/speed
    h = str(int(x//3600))
    m = str(int((x-x//3600*3600)//60))
    s = str(int((x-x//3600*3600-(x-x//3600*3600)//60*60)))
    for i in [h,m,s]:
        if len(i) ==1:
            r.append('0'+i)
        else:
            r.append(i)
    return ':'.join(r)

