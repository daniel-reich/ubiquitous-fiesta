
import re
def sync_subs(subtitles, timeIncrement):
    rc = re.compile(r'([0-1]\d|2[0-3]):[0-5]\d:[0-5]\d,\d{3}')
    if not rc.match(timeIncrement): 
        return "There is a problem with the second argument"
​
    def get_time(s):
        return int(s[:2])*3600000 + int(s[3:5])*60000 + int(s[6:8])*1000 + int(s[9:])
    def time2str(time):
        h, r = divmod(time % 86400000, 3600000)
        m, r = divmod(r, 60000)
        s, ms = divmod(r, 1000)
        return '{:02}:{:02}:{:02},{:03}'.format(h, m, s, ms)
    def add_time(match):
        return time2str(get_time(match.group(0)) + get_time(timeIncrement))
​
    return rc.sub(add_time, subtitles)

