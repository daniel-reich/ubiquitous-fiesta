
def playback_duration(duration, speed):
    s = int(sum([t * 60**(2-i) for i, t in enumerate(map(int, duration.split(':')))]) / speed)
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    return "{:02d}:{:02d}:{:02d}".format(h, m, s)

