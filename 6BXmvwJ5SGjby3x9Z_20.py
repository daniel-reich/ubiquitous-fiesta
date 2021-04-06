
def hours_passed(time1, time2):
    diff = get_hour(time2) - get_hour(time1)
    if diff == 0:
        return "no time passed"
    else:
        return str(diff) + ' hours'
​
def get_hour(txt):
    hm, ampm = txt.split()
    h, m = hm.split(':')
    h = int(h)
    if h == 12 and ampm == 'AM':
        h = 0
    elif 1 <= h <= 11 and ampm == 'PM':
        h += 12
    return h

