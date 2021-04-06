
def lets_meet(distance, va, vb):
    s = 0
    v = va + vb
    time = distance / v * 60
    timeh = time / 60
    timemin = timeh % 1
    timeh = timeh - timemin
    timemin = timemin * 60
    timesec = timemin % 1
    timemin = timemin - timesec
    timesec = timesec * 60
    time = str(int(timeh)) + "h " + str(int(timemin)) + "min " + str(int(timesec)) + "s"
    return time

