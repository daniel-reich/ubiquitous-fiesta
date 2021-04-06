
from datetime import datetime, timedelta
def palindrome_time(lst):
    h1, m1, s1, h2, m2, s2 = lst
    dt1 = datetime(1,1,1,h1, m1, s1)
    dt2 = datetime(1,1,1,h2, m2, s2)
    cnt = 0
    while dt1 <= dt2:
        t1 = dt1.strftime('%H:%M:%S')
        if t1 == t1[::-1]:
            cnt += 1
        dt1 = dt1 + timedelta(seconds=1)
    return cnt

