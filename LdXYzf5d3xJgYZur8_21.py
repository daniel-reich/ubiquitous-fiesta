
def longest_time(h, m, s):
    if h > m/60 and h > s/60/60:
        return h
    elif m/60 > h and m/60 > s/60/60:
        return m
    else:
        return s

