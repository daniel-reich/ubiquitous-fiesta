
import math
def manage_delays(train, dest, delay):
    if dest in train.destinations:
        h,m = train.expected_time.split(":")
        h = int(h)
        m = int(m)
        #print(h,m)
        m+=delay
        print(m)
        if m >= 60:
            h += math.floor(m/60)
            h = h%24
            m = m%60
        h = str(h) if h>9 else "0" + str(h)
        m = str(m) if m>9 else "0" + str(m)
        new_time = str(h) + ":" + str(m)
        train.expected_time = new_time

