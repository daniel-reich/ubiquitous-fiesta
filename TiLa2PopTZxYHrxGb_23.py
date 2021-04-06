
from math import floor
def playback_duration(duration, speed):
    t = (sum(int(i) * 60 ** (2 - ind) for ind, i in enumerate(duration.split(':'))) / speed)
    m, s = divmod(t, 60)
    h, m = divmod(m, 60)
    return ':'.join(i.rjust(2, '0') for i in map(str, map(floor, (h, m, s))))

