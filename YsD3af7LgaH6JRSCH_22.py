
def time_adjust( now, hrs, mins, sec):
    now = now.split(":")
    seconds, add = add_time(sec, int(now[2]), 60)
    mins += add
    minutes, add = add_time(mins, int(now[1]), 60)
    hrs += add
    hours, add = add_time(hrs, int(now[0]), 24)
    return format(hours) + ":" + format(minutes) + ":" + format(seconds)
​
​
def add_time(t_1, t_2, max):
    t_out = t_1 + t_2
    carry = 0
    while t_out >= max:
        carry += 1
        t_out -= max
    return t_out, carry
​
def format(time):
    out = str(time)
    if len(out) < 2:
        out = "0" + out
    return out

