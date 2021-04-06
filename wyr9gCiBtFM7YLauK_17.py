
def time_sum(times):
    retval = [0, 0, 0]
    for time in times:
        parts = time.split(':')
        if(len(parts) == 3):
            retval[0] += int(parts[0])
            retval[1] += int(parts[1])
            retval[2] += int(parts[2])
        else:
            retval.append([0, 0, 0])
​
    retval[1] += retval[2] // 60
    retval[0] += retval[1] // 60
    retval[2] = retval[2] % 60
    retval[1] = retval[1] % 60
​
    return retval

