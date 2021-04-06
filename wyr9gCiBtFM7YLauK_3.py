
from datetime import datetime
​
def time_sum(times):
    result = [0, 0, 0]
    hours = 0
    mins = 0
    secs = 0
    for i in times:
        i = i.split(':')
        hours += int(i[0])
        mins += int(i[1])
        secs += int(i[2])
​
    mins += int(secs / 60)
    secs = secs % 60
    hours += int(mins / 60)
    mins = mins % 60
    
    return [hours, mins, secs]

