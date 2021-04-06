
def time_to_eat(current_time):
​
    time = ''
    am_pm = ''
​
    if 'a.m.' in current_time:
        am_pm = 'am'
        time = current_time.replace(':', '').replace(' a.m.', '')
    else:
        am_pm = 'pm'
        time = current_time.replace(':', '').replace(' p.m.', '')
​
    h_c = int(time[:-2])
    m_c = int(time[-2:])
    if am_pm == 'am' and len(str(h_c)) == 2:
        h_c -= 12
​
    if am_pm == 'pm':
        h_c += 12
​
    times = [7, 12, 19]
    times += [h_c]
    times.sort()
    if h_c == 23:
        diff_h = times[0] + 1
    else:
        idx = times.index(h_c)
        diff_h = times[idx+1] - times[idx]
​
    diff_m = 0
    if m_c > 0:
        diff_m = 60 - m_c
        diff_h -= 1
​
    return [diff_h, diff_m]

