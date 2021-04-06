
def longest_time(h, m, s):
    d={3600*h:h,60*m:m,s:s}
    return d.get(max(d.keys()))

