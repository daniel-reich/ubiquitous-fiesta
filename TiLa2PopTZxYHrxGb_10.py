
def playback_duration(duration, speed):
    h, m, s = [int(_) for _ in duration.split(':')]
    t = int((3600 * h + 60 * m + s) / float(speed))
    h = t // 3600
    t %= 3600
    m = t // 60
    s = t % 60
    return str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)

