
def time_sum(times):
    if not times: return [0,0,0]
    h_l, m_l, s_l = zip(*[t.split(":") for t in times])
    s = sum(int(si) for si in s_l)
    m = sum(int(mi) for mi in m_l) + s//60
    h = sum(int(hi) for hi in h_l) + m//60
​
    return [h,m%60,s%60]

