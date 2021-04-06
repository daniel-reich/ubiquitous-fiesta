
import re
​
def sync_subs(subtitles, timeIncrement):
    modified = subtitles
    date_exp = re.compile(r"(\d\d\:\d\d\:\d\d\,\d\d\d)")
    date_exp2 = re.compile(r"(\d\d)\:(\d\d)\:(\d\d)\,(\d\d\d)")
    v = date_exp2.match(timeIncrement)
    if v == None:
        return "There is a problem with the second argument"
    if int(v.group(2)) >= 60 or int(v.group(3)) >= 60:
        return "There is a problem with the second argument"
    m = date_exp.findall(subtitles)
​
    chg = subtitles
    for i in range(len(m)):
        chg = chg.replace(m[i], add_times(m[i], timeIncrement))
​
    return chg
​
def add_times(time1, time2):
    date_exp = re.compile(r"(\d\d)\:(\d\d)\:(\d\d)\,(\d\d\d)")
    t1 = date_exp.match(time1)
    t2 = date_exp.match(time2)
​
    ms = int(t1.group(4)) + int(t2.group(4))
    s = int(t1.group(3)) + int(t2.group(3))
    if ms > 999:
        s += 1
        ms -= 1000
    m = int(t1.group(2)) + int(t2.group(2))
    if s > 59:
        m += 1
        s -= 60
    h = int(t1.group(1)) + int(t2.group(1))
    if m > 59:
        h += 1
        m -= 60
​
    return "{:0>2d}:{:0>2d}:{:0>2d},{:0>3d}".format(h, m, s, ms)

