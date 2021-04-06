
from datetime import timedelta
import re
​
def sync_subs(subtitles, timeIncrement):
    timeRegEx = re.compile(r'\b(0\d|1\d|2[0-3]):([0-5]\d):([0-5]\d),(\d{3})\b')
    mo_incr = timeRegEx.match(timeIncrement)
    if mo_incr == None:
        return "There is a problem with the second argument"
    else:
        match_incr = timeRegEx.findall(timeIncrement)
        h,m,s,ms = match_incr[0]
        t_incr = timedelta(
            hours=int(h),
            minutes=int(m),
            seconds=int(s),
            milliseconds=int(ms)
            )
        L = subtitles.split('\n')
        new = []
        for line in L:    
            mo_sub = timeRegEx.search(line)
            if  not mo_sub:
                new.append(line)
            else:
                match_line = line.split(' --> ')
                new_line = []
                for element in match_line:
                    match = timeRegEx.findall(element)
                    a,b,c,d = match[0]
                    t_old = timedelta(
                        hours=int(a),
                        minutes=int(b),
                        seconds=int(c),
                        milliseconds=int(d)
                        )
                    t_new = t_old + t_incr
                    H = t_new.seconds//3600
                    M = t_new.seconds%3600//60
                    S = t_new.seconds - H*3600 - M*60
                    MS = t_new.microseconds//1000
                    new_line.append('{:02}:{:02}:{:02},{}'.format(H, M, S, MS))
                    new_str = ' --> '.join(new_line)
                new.append(new_str)
    return '\n'.join(new)

