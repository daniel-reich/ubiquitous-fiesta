
def time_sum(times):
    if not times:
        return [0, 0, 0]
    secs = sum([get_secs(x) for x in times])
    h = secs // 3600
    secs = secs% 3600
    m = secs // 60
    s = secs % 60
    return [h, m, s]
    print(secs)
​
def get_secs(x):
    h, m, s = x.split(':')
    return 3600*int(h) + 60*int(m) + int(s)

