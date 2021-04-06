
def playback_duration(duration, speed):
    duration_split = duration.split(':')
    hours = int(duration_split[0])
    minutes = int(duration_split[1])
    seconds = int(duration_split[2])
    total_seconds = 0
    while hours > 0:
        total_seconds += 3600
        hours -= 1
    while minutes > 0:
        total_seconds += 60
        minutes -= 1
    total_seconds += seconds
    seconds = 0
    total_seconds = int(total_seconds / speed)
    while total_seconds >= 3600:
        hours += 1
        total_seconds -= 3600
    while total_seconds >= 60:
        minutes += 1
        total_seconds -= 60
    while total_seconds > 0:
        seconds += total_seconds
        total_seconds = 0
    return '{:02d}:{:02d}:{:02d}'.format(hours,minutes,seconds)

