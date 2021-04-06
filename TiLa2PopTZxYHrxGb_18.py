
def playback_duration(duration, speed):
    d = list(map(lambda x:int(x),duration.split(':')))
    seconds = (d[0]*3600 + d[1]*60 + d[2])/speed
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return "%02d:%02d:%02d" % (hour, min, sec)

