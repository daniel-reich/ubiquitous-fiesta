
def minutes(time):
    h, m = map(int, time.split(':'))
    return 60 * h + m
​
def sub(tt):
    diff = (minutes(tt[0]) - minutes(tt[1])) % 1440
    return "{:02}:{:02}".format(diff // 60, diff % 60)
​
def bed_time(*times):
    return list(map(sub, times))

