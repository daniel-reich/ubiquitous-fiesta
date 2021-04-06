
def time_adjust(now, hrs, mins, sec):
    count = 0
​
    time = now.split(':')
​
    seconds = sec + int(time[2])
    minutes = mins + int(time[1])
    hours = hrs + int(time[0])
​
    while seconds >= 60:
        seconds -= 60
        count += 1
    minutes += count
    count = 0
    time[2] = seconds
​
    while minutes >= 60:
        minutes -= 60
        count += 1
    hours += count
    time[1] = minutes
​
    while hours >= 24:
        hours -= 24
    time[0] = hours
​
    for n in range(3):
        if len(str(time[n])) < 2:
            time[n] = '0' + str(time[n])
        time[n] = str(time[n])
​
    return ':'.join(time)

