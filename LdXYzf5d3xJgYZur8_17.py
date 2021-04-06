
def longest_time(h, m, s):
    hour = h*60
    minute = m
    second = s/60
    if max(hour,minute,second)==hour:
        return h
    elif max(hour,minute, second)==minute:
        return m
    elif max(hour,minute,second)==second:
        return s

