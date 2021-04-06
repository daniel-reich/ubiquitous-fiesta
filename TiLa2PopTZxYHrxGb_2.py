
def playback_duration(duration, speed):
    h, m, sec = map(int, duration.split(":"))
    t = (h * 3600 + m * 60 + sec) // speed
    return "{:0>2}:{:0>2}:{:0>2}".format(int(t // 3600), int(t % 3600 // 60),
                                         int(t % 3600 % 60))

