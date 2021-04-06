
def time_adjust(now, hrs, mins, sec):
    s = int(now[-2:]) + sec
    m = int(now[3:5]) + mins + s // 60
    h = int(now[:2]) + hrs + m // 60
    h,m,s = str(h % 24),str(m % 60),str(s % 60)
    if len(str(h)) == 1: h = "0" + h
    if len(str(m)) == 1: m = "0" + m
    if len(str(s)) == 1: s = "0" + s
    return h + ":" + m + ":" + s

