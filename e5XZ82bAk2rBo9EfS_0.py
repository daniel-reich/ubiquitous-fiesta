
def bed_time(*times):
    res = []
    for wake, duration in times:
        h = int(wake[:2]) - int(duration[:2])
        s = int(wake[-2:]) - int(duration[-2:])
        res.append('{:02}:{:02}'.format((h-1)%24 if s < 0 else h%24, s%60))
    return res

