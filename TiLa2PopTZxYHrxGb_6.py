
def playback_duration(duration, speed):
    h, m, s = map(int, duration.split(':'))
    temp, seconds = divmod((3600 * h + 60 * m + s) / speed, 60)
    hours, minutes = map(int, divmod(temp, 60))
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, int(seconds))

